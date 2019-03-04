
# Shape class
# The definition of a Shape
class Shape(object):
    
    # __init__: Constructor
    # Construct the Shape
    # length: Length of the Shape
    # width: Width of the Shape
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # get_length: Getter
    # Returns the length of the Shape
    def get_length(self):
        return self.length

    # get_width: Getter
    # Returns the width of the Shape
    def get_width(self):
        return self.width

    # set_length: Setter
    # Set the length of the Shape
    def set_length(self, length):
        self.length = length

    # set_width: Setter
    # Set the width of the Shape
    def set_width(self, width):
        self.width = width

    # Area: Function
    # Calculates the Area of the Shape
    def area(self):
        return self.length * self.width

    # Perimeter: Function
    # Calculate the Perimeter of the Shape
    def perimeter(self):
        return (2 * self.length) + (2 * self.width)
        

