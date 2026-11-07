#import math
import random
import matplotlib.pyplot as plt

#TODO: Selvitä oliko kommentointi englanniksi or in finnish
#TODO: Mieti rajoja sekä liukulukujen osalta että muiden arvojen osalta. Superkolmiot, pisteiden määrä, jne.

# Wikipedian pseudokoodi algoritmin implementoinnin tueksi:
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


# Edustaa joukkoa pisteitä ja niiden välisiä särmiä
# Pisteet ovat 2D-koordinaatteja (x, y) ja särmät ovat indeksejä pisteiden listassa.
# Kolmiot ovat kolmen pisteen indeksejä, jotka muodostavat kolmion.

# All the elegant solutions I've looked up use flat arrays and pointer arithmetic
# TODO: Implement a more elegant solution with half-edges and a proper data structure for the mesh
class KonkoMesh:
    def __init__(self, points: list[tuple[float, float]]):
        self.vertices = points  # Lista pisteistä (vertices)
        self.edges = []     # Lista särmistä (edges) TODO: Muuta puolittaisiksi särmiksi (half-edges)
        self.triangles = []  # Lista kolmioista (triangles)
        pass
    
    def add_vertex(self, vertex: tuple[float, float]) -> None:
        self.vertices.append(vertex)

    def get_vertices(self) -> list[tuple[float, float]]:
        return self.vertices

    def add_edge(self, edge: tuple[int, int]) -> None:
        self.edges.append(edge)

    def get_edges(self) -> list[tuple[int, int]]:
        return self.edges

    #Tässä taitaa tulla oleelliseksi se myötäpäivään/vastapäivään aspekti, jos halutaan half-edget
    def add_triangle(self, triangle: tuple[int, int, int]) -> None:
        self.triangles.append(triangle)
        self.add_edge((triangle[0], triangle[1]))
        self.add_edge((triangle[1], triangle[2]))
        self.add_edge((triangle[2], triangle[0]))
    
    def get_triangles(self) -> list[tuple[int, int, int]]:
        return self.triangles

    def __str__(self) -> str:
        return f"Vertices: {self.vertices}\nEdges: {self.edges}\nTriangles: {self.triangles}"

# Technically this must hold up to 100 000 points.... plenty of work ahead
def create_test_points(num_points: int, width: int, height: int) -> list[tuple[float, float]]:
    points = []
    for _ in range(num_points):
        x = random.uniform(0, width)
        y = random.uniform(0, height)
        points.append((x, y))
    return points

def bowyer_watson(points: list[tuple[float, float]]) -> KonkoMesh:
    mesh = KonkoMesh(points)
    #TODO: "Write the rest of the fucking code­"
    return mesh

def matlib_visualisation(mesh: KonkoMesh) -> None:
    # Plot the points and triangles with matplotlib as dev aid 
    plt.figure()
    for triangle in mesh.get_triangles():
        vertices = [mesh.get_vertices()[i] for i in triangle]
        x_coords = [v[0] for v in vertices]
        y_coords = [v[1] for v in vertices]
        plt.fill(x_coords, y_coords, alpha=0.5)
    for vertex in mesh.get_vertices():
        plt.plot(vertex[0], vertex[1], 'o')
    plt.show()
    return

def main() -> None:
    test_points = create_test_points(6, 1000, 1000)
    #test_points = [(10, 10), (20, 30), (30, 20), (40, 40), (50, 10), (60, 30)]
    mesh = bowyer_watson(test_points)

    mesh.add_triangle((0, 1, 2))
    mesh.add_triangle((1, 2, 3))
    mesh.add_triangle((2, 3, 4))
    mesh.add_triangle((3, 4, 5))

    print(mesh)
    matlib_visualisation(mesh)

if __name__ == "__main__":
    main()