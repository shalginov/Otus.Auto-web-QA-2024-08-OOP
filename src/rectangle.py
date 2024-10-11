from figure import Figure


class Rectangle(Figure):
    """Class Rectangle"""

    def __init__(self, side_a, side_b) -> None:
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Rectangle sides can`t be less than 0")
        self.side_a = side_a
        self.side_b = side_b

    def get_area(self):
        return self.side_a * self.side_b

    def get_perimetr(self):
        return self.side_a * 2 + self.side_b * 2
