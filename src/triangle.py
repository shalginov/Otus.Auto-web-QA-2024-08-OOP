from src.figure import Figure
import math


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c) -> None:
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Triangle sides can`t be less than 0")
        if (
            side_a + side_b <= side_c
            or side_a + side_c <= side_b
            or side_b + side_c <= side_a
        ):
            raise ValueError("The triangle does not exist")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def area(self):
        sp = self.perimetr / 2  # semi perimetr
        return math.sqrt(
            sp * (sp - self.side_a) * (sp - self.side_b) * (sp - self.side_c)
        )

    @property
    def perimetr(self):
        return self.side_a + self.side_b + self.side_c
