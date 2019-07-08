from lab_python_oop.GeometricFigure import GeometricFigure as GeomF
from lab_python_oop.FigureColor import FigureColor as FigCol


class Rectangle(GeomF):
    def __init__(self,s, w, l):
        col = FigCol(s)
        self.width = w
        self.length = l
        self.color = col.color()
        self.name = 'Rectangle'

    def getname(self):
        return self.name

    def area(self):
        return self.length * self.width

    def __repr__(self):
        return "type: "+ str(self.getname())+"  width = " + str(self.width) + " length = " + str(self.length)   + " area = " + str(self.area()) + " color: " + str(self.color)
