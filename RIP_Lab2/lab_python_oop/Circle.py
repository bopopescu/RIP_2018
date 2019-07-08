from lab_python_oop.GeometricFigure import GeometricFigure
from lab_python_oop.FigureColor import FigureColor
from math import pi


class Circle(GeometricFigure):
    def __init__(self,s,r):
        self.rad = r
        col = FigureColor(s)
        self.color = col.color()
        self.name = 'Circle'
    def getname(self):
        return self.name
    def area(self):
        return self.rad * self.rad * pi
    def __repr__(self):
        return "type: " + str(self.getname()) + " radius = " + str(self.rad) + "  area = " + str(self.area()) + " color: " + str(self.color)
