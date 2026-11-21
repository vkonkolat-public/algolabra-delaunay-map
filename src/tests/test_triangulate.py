import pytest

from src.triangulate import is_point_in_circumcircle

# Basic use tests for obvious cases.
def test_point_inside_circumcircle():
    assert is_point_in_circumcircle(
        (0, 0),
        (1, 0),
        (0, 1),
        (0.5, 0.5),
    )


def test_point_outside_circumcircle():
    assert not is_point_in_circumcircle(
        (0, 0),
        (1, 0),
        (0, 1),
        (0.5, 2.5),
    )


def test_point_with_clockwise_triangle():
    assert not is_point_in_circumcircle(
        (0, 0),
        (0, 1),
        (1, 0),
        (0.5, 0.5),
    )

# Degenerate triangles are nasty cases where for example all the points are on the same line.
def test_degenerate_triangle_as_line():
    with pytest.raises(ValueError):
        is_point_in_circumcircle(
            (0, 0),
            (1, 1),
            (2, 2),
            (1, 0),
        )

# All vertices of the triangle the same point? Sounds degenerate to me.
def test_degenerate_triangle_as_point():
    with pytest.raises(ValueError):
        is_point_in_circumcircle(
            (0, 0),
            (0, 0),
            (0, 0),
            (1, 1),
        )

# Test cases for improper input
def test_improper_input_number_of_coordinates():
    with pytest.raises(ValueError):
        is_point_in_circumcircle(
            (0, 0),
            (1, 0),
            (0, 1),
            (0.5, 0.5, 0.5),  # Invalid point with three coordinates
        )

def test_improper_input_type():
    with pytest.raises(ValueError):
        is_point_in_circumcircle(
            (0, 0),
            (1, 0),
            (0, 1),
            "invalid_point",  # Invalid point type (string)
        )

def test_improper_input_non_numeric():
    with pytest.raises(TypeError):
        is_point_in_circumcircle(
            (0, 0),
            (1, 0),
            (0, 1),
            (0.5, "invalid"),  # Invalid point with non-numeric coordinate
        )

def test_improper_input_too_many_parameters():
    with pytest.raises(TypeError):
        is_point_in_circumcircle(
            (0, 0),
            (1, 0),
            (0, 1),
            (0.5, 0.5),
            (1, 1),  # Extra parameter
        )

# Tests for the get_orientation logic
# TODO: imp0lemment checking for colinear point errors
def test_get_orientation_with_collinear_points():
    from src.triangulate import get_orientation
    assert get_orientation((0, 0), (1, 1), (2, 2)) == 0  # Collinear points

def test_get_orientation_with_counterclockwise_points():
    from src.triangulate import get_orientation
    assert get_orientation((0, 0), (1, 0), (0, 1)) == 1  # Counterclockwise points

def test_get_orientation_with_clockwise_points():
    from src.triangulate import get_orientation
    assert get_orientation((0, 0), (0, 1), (1, 0)) == -1  # Clockwise points