class Student:
    """Student with name, group and average grade."""

    def __init__(self, name: str, group: str, average_grade: float):
        self.name = name
        self.group = group
        self.average_grade = average_grade

    def show_info(self) -> None:
        """Print full information about the student."""
        print(f"Name: {self.name}")
        print(f"Group: {self.group}")
        print(f"Average grade: {self.average_grade}")
        print("-" * 30)


if __name__ == "__main__":
    students = [
        Student("Ivan Petrenko", "PI-21", 4.5),
        Student("Maria Sidorenko", "PI-21", 4.8),
        Student("Peter Kovalenko", "PI-22", 3.9),
    ]

    for s in students:
        s.show_info()
