# Magic methods or Dunders
# Syntax: __methodName__
# e.g. __add__ , __sub__, __abs__ etc
# infact 5 + 6 = (5).__add__(6)
# i.e. the __add__ method is defined to add numbers
# Below we will overload the '+' operator to add two objects by redefining '__add__'

class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Coordinates(self.x + other.x, self.y + other.y)


# Objects
point1 = Coordinates(3, 5)
point2 = Coordinates(8, 11)

# Add two objects
sum = point1 + point2

print(sum.x)
print(sum.y)