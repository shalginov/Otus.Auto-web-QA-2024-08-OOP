from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle
from src.circle import Circle
import pytest

PRECISION = 0.01

add_area_test_list = [
    (1, 1, 1, 1, 5.57),
    (5, 6, 4, 4, 115.19),
]


@pytest.mark.parametrize("side_a, side_b, side_c, radius, sum_area", add_area_test_list)
def test_add_area(side_a, side_b, side_c, radius, sum_area):
    r = Rectangle(side_a, side_b)
    s = Square(side_a)
    t = Triangle(side_a, side_b, side_c)
    c = Circle(radius)
    assert sum_area - r.add_area(s) - t.add_area(c) < PRECISION


@pytest.mark.skip(reason="https://potomy4t0vot")
def test_add_area_skipped():
    r = Rectangle(4, 5)
    s = Square(4)
    assert r.add_area(s) == 72, "Get area 56 + 16 = 72"


@pytest.mark.skipif(condition=True, reason="https://potomy4t0vot2")
def test_add_area_skippedif():
    r = Rectangle(4, 5)
    s = Square(4)
    assert r.add_area(s) == 72, "Get area 56 + 16 = 72"


@pytest.mark.smoke
def test_add_area_smoked():
    r = Rectangle(7, 8)
    s = Square(5)
    assert r.add_area(s) == 81, "should be 81"


@pytest.mark.slow
def test_add_area_slowed():
    r = Rectangle(7, 8)
    s = Square(4)
    assert r.add_area(s) == 72, "should be 72"
