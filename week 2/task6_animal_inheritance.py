class Animal:
    """Base class declaring the sound() interface."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self):
        """Return the sound the animal makes.

        Subclasses must override this method.
        """
        raise NotImplementedError("Subclasses must implement sound()")


class Dog(Animal):
    def sound(self):
        return "Woof! Woof!"


class Cat(Animal):
    def sound(self):
        return "Meow! Meow!"


class Cow(Animal):
    def sound(self):
        return "Moo! Moo!"


if __name__ == "__main__":
    animals = [
        Dog("Rex", 5),
        Cat("Murka", 3),
        Cow("Burenka", 7),
    ]

    for a in animals:
        print(f"{a.__class__.__name__} {a.name} makes: {a.sound()}")
