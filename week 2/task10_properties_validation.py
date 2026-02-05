class Car:
    def __init__(self, brand: str, year: int, mileage: float = 0):
        self._brand = brand
        self._year = year
        self._mileage = mileage

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value: str):
        if not isinstance(value, str) or not value:
            raise ValueError("Brand must be a non-empty string")
        self._brand = value

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("Mileage must be a number")
        if value < 0:
            raise ValueError("Mileage cannot be negative")
        if value < self._mileage:
            raise ValueError(f"Mileage cannot decrease (current: {self._mileage})")
        self._mileage = value

    def drive(self, km: float):
        self.mileage += km

    def __str__(self):
        return f"{self.brand} ({self._year}) - {self.mileage} km"


class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        self._owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("Balance must be a number")
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def __str__(self):
        return f"{self._owner}: {self._balance} USD"


if __name__ == "__main__":
    # Car with mileage validation
    print("Car validation:")
    car = Car("Toyota", 2015, 50000)
    print(f"Initial: {car}")
    car.drive(100)
    print(f"After drive 100 km: {car}")

    try:
        car.mileage = 40000  # Attempt to decrease
    except ValueError as e:
        print(f"Error: {e}")

    try:
        car.mileage = -5000  # Attempt negative
    except ValueError as e:
        print(f"Error: {e}")

    # BankAccount with balance validation
    print("\nBankAccount validation:")
    acc = BankAccount("Alice", 1000)
    print(f"Initial: {acc}")
    acc.deposit(500)
    print(f"After deposit 500: {acc}")

    try:
        acc.balance = -100  # Attempt negative balance
    except ValueError as e:
        print(f"Error: {e}")

    try:
        acc.withdraw(2000)  # Insufficient funds
    except ValueError as e:
        print(f"Error: {e}")
