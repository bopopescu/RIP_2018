from lab_python_oop import FigureColor, GeometricFigure


class Rectangle(GeometricFigure):
    def __init__(self, s, w, h):
        col = FigureColor(s)
        self.width = w
        self.height = h
        self.color = col._color
