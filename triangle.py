# Imports
import math
from shape import Shape

# Triangle class
# Contains all of the details of the Triangle
class Triangle(Shape):

    # __init__: Constructor
    # Construcst the Triangle
    # Sides of a Triangle: a, b, c
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # set_a: Setter
    # Sets the length of a
    def set_a(self, a):
        self.a = a

    # set_b: Setter
    # Sets the length of b
    def set_b(self, b):
        self.b = b

    # set_c: Setter
    # Sets the length of c
    def set_c(self, c):
        self.c = c

    # get_a: Function
    # Returns the length of a
    def get_a(self):
        return self.a

    # get_b: Function
    # Returns the length of b
    def get_b(self):
        return self.b

    # get_c: Function
    # Returns the length of c
    def get_c(self):
        return self.c

    # area: Function
    # Calculates the area of the triangle
    def area(self):
        # Heron's Formula
        # Area = sqrt(s(s - a)(s - b)(s - c))
        # s = (a + b + c)/2
        s = self.semiperimeter()
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area

    # perimeter: Function
    # Calculates the perimeter of the triangle
    def perimeter(self):
        return self.a + self.b + self.c

    # semiperimeter: Function
    # Calculate the semiperimeter of the triangle
    def semiperimeter(self):
        return self.perimeter()/2

    # angle_ab_radians
    # Calculates the angle between a and b in radians
    def angle_ab_radians(self):
        # cos(C) = (a^2 + b^2 - c^2)/2ab
        a_squared = self.a * self.a
        b_squared = self.b * self.b
        c_squared = self.c * self.c
        return math.acos((a_squared + b_squared - c_squared)/(2 * self.a * self.b))

    # angle_bc_radians
    # Calculates the angle between b and c in radians
    def angle_bc_radians(self):
        # cos(A) = (b^2 + c^2 - a^2)/2bc
        a_squared = self.a * self.a
        b_squared = self.b * self.b
        c_squared = self.c * self.c
        return math.acos((b_squared + c_squared - a_squared)/(2 * self.b * self.c))

    # angle_ca_radians
    # Calculates the angle between c and a in radians
    def angle_ca_radians(self):
        # cos(B) = (c^2 + a^2 - b^2)/2ca
        a_squared = self.a * self.a
        b_squared = self.b * self.b
        c_squared = self.c * self.c
        return math.acos((c_squared + a_squared - b_squared)/(2 * self.c * self.a))

    # angle_ab_degrees
    # Calculates the angle between a and b in degrees
    def angle_ab_degrees(self):
        return math.degrees(self.angle_ab_radians())

    # angle_bc_degrees
    # Calculates the angle between b and c in degrees
    def angle_bc_degrees(self):
        return math.degrees(self.angle_bc_radians())

    # angle_ca_degrees
    # Calculates the angle between c and a in degrees
    def angle_ca_degrees(self):
        return math.degrees(self.angle_ca_radians())
