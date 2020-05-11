class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def reflect_x(self):
        new_point = Point(-self.x, self.y)
        return new_point

    def slope_from_origin(self):
        return self.y / self.x

    def get_line_to(self, p):
        m = (p.y - self.y)/(p.x - self.x)
        b = self.y - m * self.x
        return m, b

