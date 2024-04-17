# Class representing a Shape
class Shape:
    def __init__(self, color):
        self.color = color

# Class representing a Circle, inheriting from Shape
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

# Usage
my_circle = Circle("red", 5)
print("Area of the circle:", my_circle.area())
