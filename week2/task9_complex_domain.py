"""Library domain: Book, Reader, Librarian with class hierarchy and polymorphism."""

from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def role(self) -> str:
        pass


class Reader(Person):
    def __init__(self, name: str):
        super().__init__(name)
        self.__books = []  # Private: books borrowed

    def borrow(self, book):
        if book.is_available():
            book.borrow(self)
            self.__books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.__books:
            book.return_book()
            self.__books.remove(book)
            return True
        return False

    def get_books(self):
        return self.__books

    def role(self) -> str:
        return "Reader"


class Librarian(Person):
    def __init__(self, name: str):
        super().__init__(name)

    def add_book(self, library, book):
        library.add_book(book)

    def check_availability(self, book):
        return book.is_available()

    def role(self) -> str:
        return "Librarian"


class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.__available = True
        self.__reader = None

    def is_available(self) -> bool:
        return self.__available

    def borrow(self, reader):
        if self.__available:
            self.__available = False
            self.__reader = reader

    def return_book(self):
        self.__available = True
        self.__reader = None

    def __str__(self) -> str:
        status = "Available" if self.__available else f"Borrowed by {self.__reader.name}"
        return f"{self.title} ({self.author}) - {status}"


class Library:
    def __init__(self, name: str):
        self.name = name
        self.__books = []

    def add_book(self, book):
        self.__books.append(book)

    def get_books(self):
        return self.__books

    def list_available(self):
        return [b for b in self.__books if b.is_available()]


if __name__ == "__main__":
    lib = Library("City Library")
    lib_manager = Librarian("Alice")
    reader1 = Reader("Bob")
    reader2 = Reader("Carol")

    # Create and add books
    book1 = Book("1984", "George Orwell")
    book2 = Book("Brave New World", "Aldous Huxley")
    lib_manager.add_book(lib, book1)
    lib_manager.add_book(lib, book2)

    print(f"Library: {lib.name}")
    print(f"Librarian: {lib_manager.name} ({lib_manager.role()})")
    print(f"Initial books: {len(lib.get_books())}")

    # Borrowing
    print("\nBorrowing:")
    reader1.borrow(book1)
    reader2.borrow(book2)
    print(f"{reader1.name} borrowed: {[b.title for b in reader1.get_books()]}")
    print(f"{reader2.name} borrowed: {[b.title for b in reader2.get_books()]}")

    # Check availability
    print(f"\nAvailable books: {len(lib.list_available())}")
    for book in lib.get_books():
        print(f"  {book}")

    # Return books
    print("\nReturning:")
    reader1.return_book(book1)
    print(f"Available books after return: {len(lib.list_available())}")
    print(f"  {book1}")

    # Polymorphism: all persons have role()
    print("\nPerson roles:")
    for person in [lib_manager, reader1, reader2]:
        print(f"  {person.name}: {person.role()}")
