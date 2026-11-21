import matplotlib.pyplot as plt
import random
from konkomesh import KonkoMesh


# Creates a set of test points, later to be integrated to testing framework.
def create_test_points(num_points: int, width: int, height: int) -> list[tuple[float, float]]:
    points = []
    for _ in range(num_points):
        x = random.uniform(0, width)
        y = random.uniform(0, height)
        points.append((x, y))
    return points

# Turns a KonkoMesh into a visualisation using matplotlib. As in it opens a new window with the visualisation. 
# This is a dev aid and visual tool, not part of the actual algorithm.
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

if __name__ == "__main__": # pragma: no cover

    test_points = create_test_points(6, 1000, 1000)
    #test_points = [(10, 10), (20, 30), (30, 20), (40, 40), (50, 10), (60, 30)]
    mesh = KonkoMesh(test_points)
    mesh.add_triangle((0, 1, 2))
    mesh.add_triangle((1, 2, 3))
    mesh.add_triangle((2, 3, 4))
    mesh.add_triangle((3, 4, 5))

    print(mesh)
    matlib_visualisation(mesh)