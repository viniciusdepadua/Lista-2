class Shape:
    geometric_type = 'Generic Shape'

    def area(self):
        raise NotImplementedError

    def get_geometric_type(self):
        return self.geometric_type


class Plotter:
    def plot(self, ratio, topleft):
        print("There is no plot logic haha")


class Polygon(Shape, Plotter):
    geometric_type = 'Polygon'


"""Criando essa classe para ilustrar os diferentes MROs possíveis"""
class FourSidedPolygon(Polygon):
    geometric_type = "Four Sided Polygon"

    def __init__(self, side1, side2):
        self.width = side1
        self.lenght = side2


    def angle_sum(self):
        """Adicionando alguma utilidade para criar uma classe nova"""
        return 360


class RegularPolygon(Polygon):
    geometric_type = 'Regular Polygon'

    def __init__(self, side):
        self.side = side


class RegularHexagon(RegularPolygon):
    geometric_type = 'RegularHexagon'

    def area(self):
        return 1.5 * (3 ** .5 * self.side ** 2)


class Square(RegularPolygon, FourSidedPolygon):
    geometric_type = 'Square'

    def area(self):
        return self.side * self.side

    def angles_values(self):
        return self.angle_sum() / 4


my_square = Square(12)
print(my_square.__class__.__mro__)