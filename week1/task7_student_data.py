class Student:
    
    def __init__(self, first_name, last_name, grades):
        self.first_name = first_name
        self.last_name = last_name
        
        if len(grades) != 5:
            raise ValueError("Student must have exactly 5 grades")
        
        # Validate grades
        for grade in grades:
            if not (0 <= grade <= 100):
                raise ValueError("Grade must be between 0 and 100")
        
        self.grades = grades
    
    def average_grade(self):
        """Calculate student's average grade"""
        return sum(self.grades) / len(self.grades)
    
    def get_info(self):
        """Get student information as formatted string"""
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return f"{self.get_info()}: {self.grades} (Avg: {self.average_grade():.2f})"


class StudentGroup:
    SUBJECTS = ["Mathematics", "Physics", "Chemistry", "History", "Literature"]
    
    def __init__(self):
        """Initialize an empty student group"""
        self.students = []
    
    def add_student(self, student):
        """Add a student to the group"""
        if not isinstance(student, Student):
            raise TypeError("Only Student objects can be added")
        self.students.append(student)
    
    def remove_student(self, index):
        """Remove a student by index"""
        if 0 <= index < len(self.students):
            self.students.pop(index)
    
    def get_group_average_per_subject(self):
        """Calculate average grade for each subject across all students"""
        if not self.students:
            return [0] * 5
        
        averages = []
        for subject_idx in range(5):
            subject_grades = [student.grades[subject_idx] for student in self.students]
            averages.append(sum(subject_grades) / len(subject_grades))
        
        return averages
    
    def get_overall_group_average(self):
        """Calculate overall average grade for the entire group"""
        if not self.students:
            return 0
        
        all_grades = []
        for student in self.students:
            all_grades.extend(student.grades)
        
        return sum(all_grades) / len(all_grades)
    
    def print_group_table(self):
        if not self.students:
            print("No students in the group")
            return
        
        # Header
        header = f"{'#':<4} {'Name':<25} "
        for subject in self.SUBJECTS:
            header += f"{subject[:8]:<10} "
        header += f"{'Average':<10}"
        
        print(header)
        print("-"*100)
        
        # Student data
        for idx, student in enumerate(self.students, 1):
            row = f"{idx:<4} {student.get_info():<25} "
            for grade in student.grades:
                row += f"{grade:<10.0f} "
            row += f"{student.average_grade():<10.2f}"
            print(row)
        
        # Separator
        print("-"*100)
        
        # Group averages
        group_avgs = self.get_group_average_per_subject()
        row = f"{'AVG':<4} {'Group Average':<25} "
        for avg in group_avgs:
            row += f"{avg:<10.2f} "
        row += f"{self.get_overall_group_average():<10.2f}"
        print(row)

    def print_subject_statistics(self):
        if not self.students:
            print("No students in the group")
            return
        
        for subject_idx, subject_name in enumerate(self.SUBJECTS):
            grades = [student.grades[subject_idx] for student in self.students]
            
            avg = sum(grades) / len(grades)
            min_grade = min(grades)
            max_grade = max(grades)
            
            print(f"\n{subject_name}:")
            print(f"  Average: {avg:.2f}")
            print(f"  Minimum: {min_grade:.0f}")
            print(f"  Maximum: {max_grade:.0f}")
            print(f"  Grades: {grades}")
    
    def print_student_ranking(self):
        if not self.students:
            print("No students in the group")
            return
        
        # Sort students by average grade (descending)
        ranked = sorted(enumerate(self.students), 
                       key=lambda x: x[1].average_grade(), 
                       reverse=True)
        
        print(f"\n{'Rank':<6} {'Name':<25} {'Average Grade':<15} {'Letter Grade':<10}")
        print("-"*70)
        
        for rank, (orig_idx, student) in enumerate(ranked, 1):
            avg = student.average_grade()
            
            # Determine letter grade
            if avg >= 90:
                letter = "A"
            elif avg >= 80:
                letter = "B"
            elif avg >= 70:
                letter = "C"
            elif avg >= 60:
                letter = "D"
            else:
                letter = "F"
            
            print(f"{rank:<6} {student.get_info():<25} {avg:<15.2f} {letter:<10}")


def get_student_from_input():
    print("Enter Student Information")
    
    first_name = input("First name: ").strip()
    last_name = input("Last name: ").strip()
    
    if not first_name or not last_name:
        print("Error: Name cannot be empty")
        return None
    
    print("\nEnter 5 grades (0-100):")
    grades = []
    for subject_idx, subject in enumerate(StudentGroup.SUBJECTS):
        try:
            grade = float(input(f"  {subject_idx + 1}. {subject}: "))
            if not (0 <= grade <= 100):
                raise ValueError
            grades.append(grade)
        except ValueError:
            print(f"Error: Invalid grade. Must be between 0 and 100")
            return None
    
    try:
        return Student(first_name, last_name, grades)
    except ValueError as e:
        print(f"Error: {e}")
        return None


# Main program
# Create sample data
print("\nCreating sample student group...")
group = StudentGroup()

# Add sample students
sample_students = [
    Student("Ivan", "Petrov", [85, 90, 78, 88, 92]),
    Student("Maria", "Sidorenko", [92, 88, 95, 90, 87]),
    Student("Oleh", "Kovalenko", [78, 75, 80, 82, 79]),
    Student("Natalia", "Bondarenko", [88, 92, 89, 91, 90]),
    Student("Dmytro", "Shevchenko", [72, 68, 75, 70, 74]),
]

for student in sample_students:
    group.add_student(student)

# Display results
group.print_group_table()
group.print_subject_statistics()
group.print_student_ranking()

# Summary statistics
print("SUMMARY STATISTICS")
print(f"Total students: {len(group.students)}")
print(f"Overall group average: {group.get_overall_group_average():.2f}")

# Interactive mode
while True:
    print("\n" + "-"*50)
    print("Menu:")
    print("  1. Add new student")
    print("  2. Remove student")
    print("  3. Display group table")
    print("  4. Show subject statistics")
    print("  5. Show student ranking")
    print("  6. Show all students")
    print("  7. Quit")
    print("-"*50)
    
    choice = input("\nChoose option (1-7): ").strip()
    
    if choice == '1':
        student = get_student_from_input()
        if student:
            group.add_student(student)
            print(f"\nStudent {student.get_info()} added successfully!")
    
    elif choice == '2':
        print(f"\nCurrent students:")
        for idx, student in enumerate(group.students):
            print(f"  {idx + 1}. {student.get_info()}")
        
        try:
            remove_idx = int(input("\nEnter student number to remove: ")) - 1
            if 0 <= remove_idx < len(group.students):
                removed = group.students[remove_idx]
                group.remove_student(remove_idx)
                print(f"Student {removed.get_info()} removed successfully!")
            else:
                print("Invalid student number")
        except ValueError:
            print("Invalid input")
    
    elif choice == '3':
        group.print_group_table()
    
    elif choice == '4':
        group.print_subject_statistics()
    
    elif choice == '5':
        group.print_student_ranking()
    
    elif choice == '6':
        print(f"\nStudents in group ({len(group.students)} total):")
        for idx, student in enumerate(group.students, 1):
            print(f"  {idx}. {student}")
    
    elif choice == '7':
        break
    
    else:
        print("Invalid choice. Please try again.")