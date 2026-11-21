# The algorithm used for delaunay tringulation
# uses triangulate.py to determine if a point is inside the circumcircle of a triangle.
# Modeled after the sources cited and the pseudocode on Wikipedia: https://en.wikipedia.org/wiki/Bowyer%E2%80%93Watson_algorithm

# function BowyerWatson (pointList)
#     // pointList is a set of coordinates defining the points to be triangulated
#     triangulation := empty triangle mesh data structure
#     add super-triangle to triangulation // must be large enough to completely contain all the points in pointList
#     for each point in pointList do // add all the points one at a time to the triangulation
#         badTriangles := empty set
#         for each triangle in triangulation do // first find all the triangles that are no longer valid due to the insertion
#             if point is inside circumcircle of triangle
#                 add triangle to badTriangles
#         polygon := empty set
#         for each triangle in badTriangles do // find the boundary of the polygonal hole
#             for each edge in triangle do
#                 if edge is not shared by any other triangles in badTriangles
#                     add edge to polygon
#         for each triangle in badTriangles do // remove them from the data structure
#             remove triangle from triangulation
#         for each edge in polygon do // re-triangulate the polygonal hole
#             newTri := form a triangle from edge to point
#             add newTri to triangulation
#     for each triangle in triangulation // done inserting points, now clean up
#         if triangle contains a vertex from original super-triangle
#             remove triangle from triangulation
#     return triangulation



import triangulate
from konkomesh import KonkoMesh
import matlib_visualiser

def set_up_super_triangle(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    if not points:
        return []

    # Find the bounding box of the points
    min_x = min(point[0] for point in points)
    max_x = max(point[0] for point in points)
    min_y = min(point[1] for point in points)
    max_y = max(point[1] for point in points)

    # Calculate the size of the bounding box
    dx = max_x - min_x
    dy = max_y - min_y
    delta_max = max(dx, dy, 1)

    # Create a super triangle that encompasses all the points
    p1 = (min_x - 10 * delta_max, min_y - delta_max)
    p2 = (max_x + 10 * delta_max, min_y - delta_max)
    p3 = (min_x + 5 * delta_max, max_y + 10 * delta_max)

    return [p1, p2, p3]

def add_single_point_to_mesh(mesh: KonkoMesh, point: tuple[float, float]) -> None:
    # Step 1: Find all triangles that are no longer valid due to the insertion of the new point
    bad_triangles = []
    for triangle in mesh.get_triangles():
        A = mesh.get_vertices()[triangle[0]]
        B = mesh.get_vertices()[triangle[1]]
        C = mesh.get_vertices()[triangle[2]]
        if triangulate.get_orientation(A, B, C) < 0:
            B, C = C, B
        if triangulate.is_point_in_circumcircle(A, B, C, point):
            bad_triangles.append(triangle)

    # Step 2: Find the boundary of the polygonal hole
    edge_counts = {}
    for triangle in bad_triangles:
        edges = [
            (triangle[0], triangle[1]),
            (triangle[1], triangle[2]),
            (triangle[2], triangle[0])
        ]
        for edge in edges:
            canonical_edge = tuple(sorted(edge))
            edge_counts[canonical_edge] = edge_counts.get(canonical_edge, 0) + 1

    polygon = [edge for edge, count in edge_counts.items() if count == 1]

    # Step 3: Remove the bad triangles from the mesh
    for triangle in bad_triangles:
        mesh.triangles.remove(triangle)

    # Step 4: Re-triangulate the polygonal hole
    for edge in polygon:
        new_triangle = (edge[0], edge[1], len(mesh.get_vertices()) - 1)
        mesh.add_triangle(new_triangle)

def bowyer_watson(points: list[tuple[float, float]]) -> KonkoMesh:
    if not points:
        return KonkoMesh([])

    # if the number of points is less than 3, we cannot form a triangle, so we return an empty mesh
    if len(points) < 3:
        print("Not enough points to form a triangle. Returning an empty mesh.")
        return KonkoMesh([])

    # Step 0: Create a super triangle that encompasses all the points
    super_triangle = set_up_super_triangle(points)
    mesh = KonkoMesh(super_triangle)
    mesh.add_triangle((0, 1, 2))

    # Step 1: Add each point to the mesh
    for point in points:
        mesh.add_vertex(point)
        add_single_point_to_mesh(mesh, point)

    # Step 2: Remove triangles that contain vertices of the super triangle
    super_triangle_indices = {0, 1, 2}
    triangles = [
        tuple(v - 3 if v >= 3 else v for v in triangle)
        for triangle in mesh.get_triangles()
        if not any(v in super_triangle_indices for v in triangle)
    ]

    # step 3: Remove the vertices of the super triangle and reindex the triangles
    mesh.vertices = list(points)
    mesh.triangles = triangles
    mesh.edges = []
    for triangle in triangles:
        mesh.add_edge((triangle[0], triangle[1]))
        mesh.add_edge((triangle[1], triangle[2]))
        mesh.add_edge((triangle[2], triangle[0]))

    return mesh

def main() -> None:
    # internal printing test cases
    test_cases = [
        ([], 0),
        ([(0, 0)], 0),
        ([(0, 0), (1, 0), (0, 1)], 1),
        ([(0, 0), (1, 0), (0, 1), (1, 1)], 2),
    ]

    for points, expected_triangle_count in test_cases:
        mesh = bowyer_watson(points)
        triangle_count = len(mesh.get_triangles())
        assert triangle_count == expected_triangle_count, (
            f"Expected {expected_triangle_count} triangles for {points}, "
            f"got {triangle_count}"
        )
        print(f"Points: {points}")
        print(mesh)

    # visualisation test case
    # As of 2026-11-21 produces a stable triangulation for 10 points without visual glitches and no crashes.abs
    # No stress tetsts for perverse behaviour done yet, TODO: maybe 1000 points looking for abnormal exit
    random_points = matlib_visualiser.create_test_points(10, 100, 100)
    mesh = bowyer_watson(random_points)
    matlib_visualiser.matlib_visualisation(mesh)


if __name__ == "__main__": # pragma: no cover
    main()
