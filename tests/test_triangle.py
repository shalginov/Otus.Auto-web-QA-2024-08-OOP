from src.triangle import Triangle
import pytest

PRECISION = 0.01

area_test_list = [
    (4, 5, 6, 9.92),
    (1, 1, 1, 0.43),
    (0, 1, 1, 0),
    (1, 0, 1, 0),
    (1, 1, 0, 0),
    (2, 1, 1, 0),
    (1, 2, 1, 0),
    (1, 1, 2, 0),
    (-1, 1, 1, 0),
    (1, -1, 1, 0),
    (1, 1, -1, 0),
]


@pytest.mark.parametrize("side_a, side_b, side_c, expect_area", area_test_list)
def test_area_triangle(side_a, side_b, side_c, expect_area):
    t = Triangle(side_a, side_b, side_c)
    assert expect_area - t.area < PRECISION


perimetr_test_list = [
    (4, 5, 6, 15),
    (1, 1, 1, 3),
    (0, 1, 1, 0),
    (1, 0, 1, 0),
    (1, 1, 0, 0),
    (-1, 1, 1, 0),
    (1, -1, 1, 0),
    (1, 1, -1, 0),
    (2, 1, 1, 0),
    (1, 2, 1, 0),
    (1, 1, 2, 0),
]


@pytest.mark.parametrize("side_a, side_b, side_c, expect_perimetr", perimetr_test_list)
def test_perimetr_triangle(side_a, side_b, side_c, expect_perimetr):
    t = Triangle(side_a, side_b, side_c)
    assert t.perimetr == expect_perimetr, f"Perimetr should be {expect_perimetr}"
