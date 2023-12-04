from typing import Optional, Tuple
from xml.etree.ElementTree import register_namespace, XML, tostring
from svg.core import CompositeItem, Drawable


class Drawing():
    def __init__(self, width=640, height=480, view_box:Optional[Tuple[int, int, int, int]] = None):
        self.width = width
        self.height = height
        self.view_box = view_box
        register_namespace("", "http://www.w3.org/2000/svg")

        if self.view_box:
            vb = ' viewBox="%d %d %d %d"' % self.view_box
        else:
            vb = ''
        self.xml = XML('<svg width="%d" height="%d" version="1.1" xmlns="http://www.w3.org/2000/svg"%s></svg>' %
                       (self.width, self.height, vb))

    def add(self, child: Drawable):
        element = child.element()
        self.xml.append(element)

    def svg(self):
        xml = self.xml
        result = tostring(xml).decode('utf-8')
        return result
