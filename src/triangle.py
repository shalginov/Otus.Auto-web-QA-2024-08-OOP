from figure import Figure
import math


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c) -> None:
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Triangle sides can`t be less than 0")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        sp = self.get_perimetr() / 2  # sime perimetr
        return math.sqrt(
            sp * (sp - self.side_a) * (sp - self.side_b) * (sp - self.side_c)
        )

    def get_perimetr(self):
        return self.side_a + self.side_b + self.side_c
