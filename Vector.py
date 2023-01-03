import math
class Vector:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def magnitude(self):
        return math.sqrt(self.x**2+self.y**2)
    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)
    def __sub__(self, other):
        return Vector(self.x-other.x, self.y-other.y)
    def __str__(self):
        return f"({self.x}, {self.y})"

a=Vector(1,0)
b=Vector(3,4)
c=a+b
print(c)
