class Car:
    """Minimal Car class: brand, year, mileage, with drive and info."""

    def __init__(self, brand: str, year: int, mileage: int = 0):
        self.brand = brand
        self.year = year
        self.mileage = mileage

    def drive(self, km: int) -> None:
        """Increase mileage by km (only positive values)."""
        if km > 0:
            self.mileage += km

    def info(self) -> None:
        """Print a short description of the car."""
        print(f"Brand: {self.brand}")
        print(f"Year: {self.year}")
        print(f"Mileage: {self.mileage} km")

    def __str__(self) -> str:
        return f"{self.brand} ({self.year}) - {self.mileage} km"


if __name__ == "__main__":
    c1 = Car("Toyota Camry", 2015, 120000)
    c2 = Car("BMW X5", 2020, 35000)
    c3 = Car("Lada Granta", 2022)

    # Demo
    print(c1)
    c1.drive(150)
    print("After drive:")
    c1.info()

    print()
    print(c3)
    c3.drive(500)
    print("After drive:")
    c3.info()
