from src.circle import Circle
import pytest

PRECISION = 0.01

radius_value_error_list = [0, -1]


@pytest.mark.parametrize("radius", radius_value_error_list)
def test_radius_value_error(radius):
    with pytest.raises(ValueError) as err:
        Circle(radius)
    assert "The radius can`t be less than 0" == str(err.value)


area_test_list = [
    (4, 50.27),
    (1, 3.14),
    (1.56, 7.65),
]


@pytest.mark.parametrize("radius, expect_area", area_test_list)
def test_area_circle(radius, expect_area):
    c = Circle(radius)
    assert expect_area - c.area < PRECISION, f"Area shold be {expect_area}"


perimetr_test_list = [
    (4, 25.13),
    (1, 6.28),
    (1, 6.28),
    (1.56, 9.8),
]


@pytest.mark.parametrize("radius, expect_perimetr", perimetr_test_list)
def test_perimetr_circle(radius, expect_perimetr):
    c = Circle(radius)
    assert (
        expect_perimetr - c.perimetr < PRECISION
    ), f"Perimetr should be {expect_perimetr}"
