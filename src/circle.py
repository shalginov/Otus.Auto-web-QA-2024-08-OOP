from src.figure import Figure
import math


class Circle(Figure):
    def __init__(self, radius) -> None:
        if radius <= 0:
            raise ValueError("The radius can`t be less than 0")
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius**2

    @property
    def perimetr(self):
        return 2 * math.pi * self.radius
