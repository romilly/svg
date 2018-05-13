from _elementtree import Element
from abc import ABCMeta, abstractmethod

from svg.point import Point
from svg.svg import SimpleItem




class Path(SimpleItem):
    def __init__(self, start, *segments, **attributes):
        SimpleItem.__init__(self, start)
        self.segments = segments
        self.closed = True # can set to false if open path required
        self._attributes = attributes

    def element(self):
        p = Element('path',**self._attributes)
        d = 'M %s ' % self.top_left.format()
        d += ' '.join([segment.specification() for segment in self.segments])
        if self.closed:
            d += ' Z'
        p.set('d', d)
        if 'width' in self._attributes:
            p.set('stroke-width', self._attributes['width'])
        return p


class PathSegment():
    __metaclass__ = ABCMeta

    @abstractmethod
    def specification(self):
        pass


class RelativeVector(PathSegment):
    def __init__(self, x, y):
        self.point = Point(x,y)

    def specification(self):
        return 'l %s ' % self.point.format()

    def scale(self,scale):
        self.point= self.point.scale(scale)
        return self


def vector(x, y):
    return RelativeVector(x,y)


class Arc(PathSegment):
    def __init__(self, x, y, xrot, large_arc, sweep, endx, endy):
        self._spec = (x, y, xrot, large_arc, sweep, endx, endy)

    def specification(self):
        return 'a %f %f, %f, %d, %d, %f, %f' % self._spec


def arc(x, y, xrot, large_arc, sweep, endx, endy):
    return Arc(x, y, xrot, large_arc, sweep, endx, endy)

