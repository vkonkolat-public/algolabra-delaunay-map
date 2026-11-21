import unittest
from src.konkomesh import KonkoMesh

class TestKonkoMesh(unittest.TestCase):
    def setUp(self):
        self.points = [(0, 0), (1, 0), (0, 1), (1, 1)]
        self.mesh = KonkoMesh(self.points)

    def test_add_triangle(self):
        self.mesh.add_triangle((0, 1, 2))
        self.assertIn((0, 1, 2), self.mesh.get_triangles())

    def test_get_triangles(self):
        self.mesh.add_triangle((0, 1, 2))
        triangles = self.mesh.get_triangles()
        self.assertEqual(triangles, [(0, 1, 2)])

    def test_add_vertex(self):
        self.mesh.add_vertex((2, 2))
        self.assertIn((2, 2), self.mesh.get_vertices())

    def test_get_vertices(self):
        vertices = self.mesh.get_vertices()
        self.assertEqual(vertices, self.points)

    def test_add_edge(self):
        self.mesh.add_edge((0, 1))
        self.assertIn((0, 1), self.mesh.get_edges())

    def test_get_edges(self):
        self.mesh.add_edge((0, 1))
        edges = self.mesh.get_edges()
        self.assertEqual(edges, [(0, 1)])

    def test_str_representation(self):
        self.mesh.add_triangle((0, 1, 2))
        expected_str = "Vertices: [(0, 0), (1, 0), (0, 1), (1, 1)]\nEdges: [(0, 1), (1, 2), (2, 0)]\nTriangles: [(0, 1, 2)]"
        self.assertEqual(str(self.mesh), expected_str)
