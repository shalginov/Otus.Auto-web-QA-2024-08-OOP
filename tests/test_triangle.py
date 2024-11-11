from src.triangle import Triangle
import pytest

PRECISION = 0.01

sides_not_exist_tr_list = [
    (2, 1, 1),
    (1, 2, 1),
    (1, 1, 2),
]


@pytest.mark.parametrize("side_a, side_b, side_c", sides_not_exist_tr_list)
def test_not_exist_triangle(side_a, side_b, side_c):
    with pytest.raises(ValueError) as err:
        Triangle(side_a, side_b, side_c)
    assert "The triangle does not exist" == str(err.value)


sides_value_error_list = [
    (0, 1, 1),
    (1, 0, 1),
    (1, 1, 0),
    (-1, 1, 1),
    (1, -1, 1),
    (1, 1, -1),
]


@pytest.mark.parametrize("side_a, side_b, side_c", sides_value_error_list)
def test_sides_value_error(side_a, side_b, side_c):
    with pytest.raises(ValueError) as err:
        Triangle(side_a, side_b, side_c)
    assert str(err.value) == "Triangle sides can`t be less than 0"


area_test_list = [
    (4, 5, 6, 9.92),
    (1, 1, 1, 0.43),
]


@pytest.mark.parametrize("side_a, side_b, side_c, expect_area", area_test_list)
def test_area_triangle(side_a, side_b, side_c, expect_area):
    t = Triangle(side_a, side_b, side_c)
    assert expect_area - t.area < PRECISION


perimetr_test_list = [
    (4, 5, 6, 15),
    (1, 1, 1, 3),
]


@pytest.mark.parametrize("side_a, side_b, side_c, expect_perimetr", perimetr_test_list)
def test_perimetr_triangle(side_a, side_b, side_c, expect_perimetr):
    t = Triangle(side_a, side_b, side_c)
    assert t.perimetr == expect_perimetr, f"Perimetr should be {expect_perimetr}"
