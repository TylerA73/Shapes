# Imports
import math
from shape import Shape

# Circle class
# Contains the details of the Circle
class Circle(Shape):
    
    #__init__: Constructor
    # Constructs the circle
    def __init__(self, radius):
        self.radius = radius

    # set_radius: Setter
    # Sets the radius of the circle
    def set_radius(self, radius):
        self.radius = radius

    # get_radius: Getter
    # Returns the radius of the circle
    def get_radius(self):
        return self.radius
    
    # diameter: Function
    # Calculates and returns the diameter of the circle
    def diameter(self):
        return 2 * self.radius

    # circumference: Function
    # Calculates and returns the circumference of the circle
    def circumference(self):
        return math.pi * self.diameter()
