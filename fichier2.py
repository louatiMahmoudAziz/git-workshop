import math
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

u = Vector(int(input("Enter x-coordinate 1: ")), int(input("Enter y-coordinate 1: ")))
v = Vector(int(input("Enter x-coordinate 2: ")), int(input("Enter y-coordinate 2: ")))

print(u + v)
