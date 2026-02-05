class Animal:
    def __init__(self, name: str):
        self.name = name

    def sound(self) -> str:
        return "<silent>"


class Dog(Animal):
    def sound(self) -> str:
        return "Woof!"


class Cat(Animal):
    def sound(self) -> str:
        return "Meow!"


class Cow(Animal):
    def sound(self) -> str:
        return "Moo!"


if __name__ == "__main__":
    animals = [Dog("Rex"), Cat("Murka"), Cow("Burenka")]

    print("Polymorphism (Late Binding):")
    for a in animals:
        print(f"{a.__class__.__name__} {a.name} -> {a.sound()}")

    print("\nExplanation: Python dynamically chooses which sound() method to call")
    print("based on the actual object type at runtime, not at compile time.")