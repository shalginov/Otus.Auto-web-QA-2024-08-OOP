from src.square import Square
import pytest


side_value_error_list = [0, -1]


@pytest.mark.parametrize("side_a", side_value_error_list)
def test_side_value_error(side_a):
    with pytest.raises(ValueError) as err:
        Square(side_a)
    assert "Square sides can`t be less than 0" == str(err.value)


area_test_list = [
    (5, 25),
    (1, 1),
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
]


@pytest.mark.parametrize("side_a, expect_perimetr", perimetr_test_list)
def test_perimetr_square(side_a, expect_perimetr):
    s = Square(side_a)
    assert s.perimetr == expect_perimetr, f"Perimetr should be {expect_perimetr}"
