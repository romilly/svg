from abc import ABC, abstractmethod

from svg.point import Point
from math import sin, cos, radians


class Transform(ABC):
    """Represents an atomic svg transformation - a translation, rotation or scaling"""

    @abstractmethod
    def text(self):
        pass

    @abstractmethod
    def as_matrix(self):
        pass

    @abstractmethod
    def transform(self, point):
        pass


class Translation(Transform):
    def __init__(self, vector):
        self.vector = vector

    def text(self):
        return 'translate(%f,%f)' % (self.vector.cartesian_coordinates())

    def as_matrix(self):
        return

    def transform(self, point):
        return point + self.vector


class Rotation(Transform):
    def as_matrix(self):
        pass

    def __init__(self, angle, origin=Point(0, 0)):
        self.angle = angle
        self.origin = origin

    def text(self):
        return 'rotate(%f,%f,%f)' % (self.angle, self.origin.x, self.origin.y)

    def transform(self, point):
        p = point
        s = sin(radians(-self.angle))
        c = cos(radians(-self.angle))
        point1 = Point(c*p.x + s * p.y, (c*p.y - s*p.x))
        result = point1
        return result
