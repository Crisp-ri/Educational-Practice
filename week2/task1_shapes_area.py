import math

#Procedural approach
def area_rectangle(width, height):
    return width * height


def area_circle(radius):
    return math.pi * radius * radius


#OOP approach
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


if __name__ == "__main__":
    # Procedural
    print("Procedural approach:")
    print(f"Rectangle 3x4 area = {area_rectangle(3, 4)}")
    print(f"Circle r=2 area = {area_circle(2):.4f}")

    # OOP
    print("\nOOP approach:")
    r = Rectangle(3, 4)
    c = Circle(2)
    print(f"Rectangle(3,4).area() = {r.area()}")
    print(f"Circle(2).area() = {c.area():.4f}")
