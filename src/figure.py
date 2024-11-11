from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetr(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Should be a figure")
        return self.area + other_figure.area
