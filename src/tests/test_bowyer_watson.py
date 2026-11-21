from src import bowyer_watson

def test_super_triangle_set_up():
    points = [(0, 0), (1, 0), (0, 1)]
    super_triangle = bowyer_watson.set_up_super_triangle(points)
    assert len(super_triangle) == 3
    assert all(isinstance(p, tuple) and len(p) == 2 for p in super_triangle)

def test_super_triangle_with_collinear_points():
    points = [(0, 0), (1, 0), (2, 0)]
    super_triangle = bowyer_watson.set_up_super_triangle(points)
    assert len(super_triangle) == 3
    assert all(isinstance(p, tuple) and len(p) == 2 for p in super_triangle)

def test_super_triangle_with_negative_coordinates():
    points = [(-1, -1), (-2, -3), (-4, -5)]
    super_triangle = bowyer_watson.set_up_super_triangle(points)
    assert len(super_triangle) == 3
    assert all(isinstance(p, tuple) and len(p) == 2 for p in super_triangle)

# Properly check if the super triangle is large enough
def test_super_triangle_with_one_very_large_point():
    points = [(0, 0), (1, 1), (10000, 10000)]
    super_triangle = bowyer_watson.set_up_super_triangle(points)
    assert len(super_triangle) == 3
    assert all(isinstance(p, tuple) and len(p) == 2 for p in super_triangle)
    super_x = [point[0] for point in super_triangle]
    super_y = [point[1] for point in super_triangle]
    assert min(super_x) <= 0 and max(super_x) >= 10000
    assert min(super_y) <= 0 and max(super_y) >= 10000

# Add one point in the middle of a triangle and check if the old triangle and edges are removed and new triangles are added
def test_add_single_point_to_mesh():
    dummy_konkomesh = bowyer_watson.KonkoMesh([(0, 0), (1, 0), (0, 1)])
    dummy_konkomesh.add_triangle((0, 1, 2))
    point = (0.5, 0.5)
    bowyer_watson.add_single_point_to_mesh(dummy_konkomesh, point)
    assert point in dummy_konkomesh.get_vertices()
    assert (0, 1, 3) in dummy_konkomesh.get_triangles()
    assert (1, 2, 3) in dummy_konkomesh.get_triangles()
    assert (0, 2, 3) in dummy_konkomesh.get_triangles()

def test_bowyer_watson_empty():
    points = []
    mesh = bowyer_watson.bowyer_watson(points)
    assert len(mesh.get_vertices()) == 0
    assert len(mesh.get_triangles()) == 0

def test_bowyer_watson_improper_input_typeerror():
    points = "not a list of tuples"
    try:
        bowyer_watson.bowyer_watson(points)
        assert False, "Expected TypeError"
    except TypeError:
        pass

# Figure out how to test the visualisation logic and automatically close the window. Mock patch and inserting plt as dependecy considered.
# Partial success, at least the window no longer opens.
from unittest.mock import patch
@patch("src.bowyer_watson.matlib_visualiser.matlib_visualisation")
def test_main(mock_visualisation):
    bowyer_watson.main()
    mock_visualisation.assert_called_once()