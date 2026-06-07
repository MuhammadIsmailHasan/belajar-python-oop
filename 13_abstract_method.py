from abc import ABC, abstractmethod

class Shape(ABC) :

    @abstractmethod
    def area(self):
        pass

    # wajib di implementasikan dalam class child


class Rectangle(Shape) :
    def __init__(self, a, b) :
        self.a = a
        self.b = b

    def area(self) :
        return self.a * self.b

class Triangle(Shape) :
    def __init__(self, a, b, c) :
        self.a = a
        self.b = b
        self.c = c

    def area(self) :
        return self.a * self.b * self.c

shape_list = [
    Rectangle(1, 2),
    Triangle(2, 3, 4),
]

for shape in shape_list :
    print(shape.area())