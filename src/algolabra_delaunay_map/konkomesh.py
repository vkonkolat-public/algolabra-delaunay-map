# KonkoMesh class is for representing a mesh of triangles, edges, and vertices in 2D space.
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

    # Tässä taitaa tulla oleelliseksi se myötäpäivään/vastapäivään aspekti, jos halutaan half-edget
    # 14.11.2026 triangulate.py can now tell whether a triangle is clockwise or counterclockwise
    def add_triangle(self, triangle: tuple[int, int, int]) -> None:
        self.triangles.append(triangle)
        self.add_edge((triangle[0], triangle[1]))
        self.add_edge((triangle[1], triangle[2]))
        self.add_edge((triangle[2], triangle[0]))
    
    def get_triangles(self) -> list[tuple[int, int, int]]:
        return self.triangles

    def __str__(self) -> str:
        return f"Vertices: {self.vertices}\nEdges: {self.edges}\nTriangles: {self.triangles}"