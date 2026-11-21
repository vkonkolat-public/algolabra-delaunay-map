import pytest

from src.triangulate import is_point_in_circumcircle


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


def test_point_with_degenerate_triangle():
    with pytest.raises(ValueError):
        is_point_in_circumcircle(
            (0, 0),
            (1, 1),
            (2, 2),
            (1, 0),
        )


