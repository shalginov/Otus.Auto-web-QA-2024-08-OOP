from figure import Figure
import math


class Circle(Figure):
    def __init__(self, radius) -> None:
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ^ 2

    def get_perimetr(self):
        return 2 * math.pi * self.radius
