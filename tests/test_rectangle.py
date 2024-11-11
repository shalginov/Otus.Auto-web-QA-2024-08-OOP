from src.rectangle import Rectangle
import pytest

sides_value_error_list = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]


@pytest.mark.parametrize("side_a, side_b", sides_value_error_list)
def test_sides_value_error(side_a, side_b):
    with pytest.raises(ValueError) as err:
        Rectangle(side_a, side_b)
    assert "Rectangle sides can`t be less than 0" == str(err.value)


area_test_list = [
    (5, 6, 30),
    (1, 1, 1),
]


@pytest.mark.parametrize("side_a, side_b, expect_area", area_test_list)
def test_area_rectangle(side_a, side_b, expect_area):
    r = Rectangle(side_a, side_b)
    assert r.area == expect_area, f"Area should be  {expect_area}"


perimetr_test_list = [
    (5, 6, 22),
    (1, 1, 4),
]


@pytest.mark.parametrize("side_a, side_b, expect_perimetr", perimetr_test_list)
def test_perimetr_rectangle(side_a, side_b, expect_perimetr):
    r = Rectangle(side_a, side_b)
    assert r.perimetr == expect_perimetr, f"Perimetr should be {expect_perimetr}"
