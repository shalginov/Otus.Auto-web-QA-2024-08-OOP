from src.square import Square
import pytest

area_test_list = [
    (5, 25),
    (1, 1),
    (0, 0),
    (-1, 0),
]


@pytest.mark.parametrize("side_a, expect_area, ", area_test_list)
def test_area_square(
    side_a,
    expect_area,
):
    s = Square(side_a)
    assert s.area == expect_area, f"Area should be {expect_area}"


perimetr_test_list = [
    (6, 24),
    (1, 4),
    (0, 0),
    (-1, 0),
]


@pytest.mark.parametrize("side_a, expect_perimetr", perimetr_test_list)
def test_perimetr_square(side_a, expect_perimetr):
    s = Square(side_a)
    assert s.perimetr == expect_perimetr, f"Perimetr should be {expect_perimetr}"
