# Imports
from shape import Shape
from square import Square
from circle import Circle
from triangle import Triangle

# Create the Shape
shape = Shape(5, 3)

# Print the details of the Shape
print("SHAPE")
print("Length:", shape.get_length()) # length = 5
print("Width:", shape.get_width()) # width = 3
print("Area:", shape.area()) # area = 15
print("Perimeter:", shape.perimeter()) # perimeter = 16
print()

# Change the details of the Shape
shape.set_length(10)
shape.set_width(5)

# Print the new details of the Shape
print("SHAPE 2")
print("Length:", shape.get_length()) # length = 10
print("Width:", shape.get_width()) # width = 5
print("Area:", shape.area()) # area = 50
print("Perimeter:", shape.perimeter()) # perimeter = 30
print()

# Create the Square
square = Square(5)

# Print the details of the Square
print("SQUARE")
print("Length:", square.get_length()) # length = 5
print("Area:", square.area()) # area = 25
print("Perimeter:", square.perimeter()) # perimeter = 20
print()

# Create the Circle
circle = Circle(3)

# Print the details of the Circle
print("CIRCLE")
print("Radius:", circle.get_radius()) # radius = 3
print("Diameter:", circle.diameter()) # diameter = 6
print("Circumference:", circle.circumference()) # circumference ~= 18.85
print()

# Create the Triangle
triangle = Triangle(3, 4, 5)

# Print the details of the Triangle
print("TRIANGLE")
print("A:", triangle.get_a()) # a = 3
print("B:", triangle.get_b()) # b = 4
print("C:", triangle.get_c()) # c = 5
print("Angle AB (Radians):", triangle.angle_ab_radians())
print("Angle AB (Degrees):", triangle.angle_ab_degrees())
print("Angle BC (Radians):", triangle.angle_bc_radians())
print("Angle BC (Degrees):", triangle.angle_bc_degrees())
print("Angle CA (Radians):", triangle.angle_ca_radians())
print("Angle CA (Degrees):", triangle.angle_ca_degrees())
print("Area:", triangle.area())
print("Perimeter:", triangle.perimeter())
print("Semiperimeter:", triangle.semiperimeter())

