"""location_of must agree with how SVG applies a transform list:
transform="A B" maps a point through B first, then A."""
import pytest

from svg.core import GroupedDrawable
from svg.point import Point


def located(drawable, x, y):
    p = drawable.location_of(Point(x, y))
    return pytest.approx(p.x), pytest.approx(p.y)


def test_translation():
    g = GroupedDrawable().move_to(Point(30, 40))
    assert located(g, 1, 2) == (31, 42)


def test_rotation_about_origin_point():
    g = GroupedDrawable().rotate(90, Point(10, 10))
    assert located(g, 20, 10) == (10, 20)


def test_rotate_then_move_to_when_points_coincide():
    g = GroupedDrawable().rotate(-90, Point(40, 400)).move_to(Point(40, 400))
    assert located(g, 10, 0) == (40, 390)


def test_rotate_then_move_to_when_points_differ():
    # SVG: rotate(-90 about (40,400)) applied to (P + (80,400))
    g = GroupedDrawable().rotate(-90, Point(40, 400)).move_to(Point(80, 400))
    assert located(g, 0, 0) == (40, 360)
    assert located(g, 10, 0) == (40, 350)
