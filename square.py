# Imports
from shape import Shape

# Square class
# Details of the Square
# Child of the Shape class
class Square(Shape):

    # __init__: Constructor
    # Constructs the Square
    def __init__(self, length):
        self.length = length

    # area: Function
    # Calculates and returns the area of the Square
    def area(self):
        return self.length * self.length

    # perimeter: Function
    # Calculate and returns the perimeter of the Square
    def perimeter(self):
        return self.length * 4


