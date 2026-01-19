import pandas as pd
import os
from pathlib import Path


class StudentDataManager:
    SUBJECTS = ["Mathematics", "Physics", "Chemistry", "History", "Literature"]
    
    def __init__(self, filepath="students.csv"):
        self.filepath = filepath
        self.df = None
        self.load_data()
    
    def load_data(self):
        """Load student data from CSV file"""
        if os.path.exists(self.filepath):
            self.df = pd.read_csv(self.filepath)
            print(f"Loaded {len(self.df)} students from {self.filepath}")
        else:
            # Create empty DataFrame with columns
            columns = ["First Name", "Last Name"] + self.SUBJECTS
            self.df = pd.DataFrame(columns=columns)
            print(f"Created new student database at {self.filepath}")
    
    def save_data(self):
        """Save student data to CSV file"""
        self.df.to_csv(self.filepath, index=False)
        print(f"Data saved to {self.filepath}")
    
    def add_student(self, first_name, last_name, grades):
        """Add a new student to the database"""
        
        if len(grades) != 5:
            raise ValueError("Student must have exactly 5 grades")
        
        # Check if student already exists
        existing = self.df[(self.df["First Name"] == first_name) & 
                          (self.df["Last Name"] == last_name)]
        if not existing.empty:
            print(f"Warning: Student {first_name} {last_name} already exists!")
            return False
        
        # Add new row
        new_row = {
            "First Name": first_name,
            "Last Name": last_name,
        }
        for idx, grade in enumerate(grades):
            new_row[self.SUBJECTS[idx]] = grade
        
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)
        return True
    
    def remove_student(self, first_name, last_name):
        """Remove a student from the database"""
        initial_len = len(self.df)
        self.df = self.df[~((self.df["First Name"] == first_name) & 
                           (self.df["Last Name"] == last_name))]
        
        if len(self.df) < initial_len:
            print(f"Removed {first_name} {last_name}")
            return True
        else:
            print(f"Student {first_name} {last_name} not found")
            return False
    
    def add_average_column(self):
        """Add average grade column"""
        self.df["Average"] = self.df[self.SUBJECTS].mean(axis=1)
        return self.df
    
    def get_group_statistics(self):
        """Get statistics for the entire group"""
        
        if self.df.empty:
            print("No students in database")
            return None
        
        stats = {}
        
        # Overall average
        stats["Overall Average"] = self.df[self.SUBJECTS].values.flatten().mean()
        
        # Average by subject
        stats["Subject Averages"] = self.df[self.SUBJECTS].mean()
        
        # Student averages
        stats["Student Averages"] = self.df[self.SUBJECTS].mean(axis=1)
        
        return stats
    
    def display_table(self):
        """Display formatted table with all student data"""
        
        print("\n" + "="*120)
        print("STUDENT GROUP STATISTICS TABLE")
        print("="*120 + "\n")
        
        if self.df.empty:
            print("No students in database")
            return
        
        # Add average column for display
        df_display = self.df.copy()
        df_display["Average"] = df_display[self.SUBJECTS].mean(axis=1)
        
        # Format for display
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', None)
        
        # Create formatted output
        print(df_display.to_string(index=True))
        
        # Add summary row
        print("\n" + "-"*120)
        summary = {"First Name": "GROUP AVG", "Last Name": ""}
        for subject in self.SUBJECTS:
            summary[subject] = df_display[subject].mean()
        summary["Average"] = df_display[self.SUBJECTS].values.flatten().mean()
        
        summary_df = pd.DataFrame([summary])
        print(summary_df.to_string(index=False))
        print("="*120)
    
    def display_subject_statistics(self):
        """Display detailed statistics for each subject"""
        
        print("\n" + "="*70)
        print("SUBJECT STATISTICS")
        print("="*70 + "\n")
        
        if self.df.empty:
            print("No students in database")
            return
        
        for subject in self.SUBJECTS:
            data = self.df[subject]
            
            print(f"{subject}:")
            print(f"  Average:  {data.mean():.2f}")
            print(f"  Minimum:  {data.min():.0f}")
            print(f"  Maximum:  {data.max():.0f}")
            print(f"  Std Dev:  {data.std():.2f}")
            print(f"  Median:   {data.median():.2f}")
            print()
    
    def display_ranking(self):
        """Display students ranked by average grade"""
        
        print("\n" + "="*80)
        print("STUDENT RANKING (by average grade)")
        print("="*80 + "\n")
        
        if self.df.empty:
            print("No students in database")
            return
        
        # Create ranking dataframe
        rank_df = self.df.copy()
        rank_df["Average"] = rank_df[self.SUBJECTS].mean(axis=1)
        rank_df = rank_df.sort_values("Average", ascending=False)
        rank_df["Rank"] = range(1, len(rank_df) + 1)
        
        # Add letter grades
        def get_letter_grade(avg):
            if avg >= 90:
                return "A"
            elif avg >= 80:
                return "B"
            elif avg >= 70:
                return "C"
            elif avg >= 60:
                return "D"
            else:
                return "F"
        
        rank_df["Grade"] = rank_df["Average"].apply(get_letter_grade)
        
        # Display
        display_cols = ["Rank", "First Name", "Last Name", "Average", "Grade"]
        print(rank_df[display_cols].to_string(index=False))
        print("="*80)
    
    def export_to_csv(self, filename=None):
        """Export data to CSV file"""
        if filename is None:
            filename = self.filepath
        self.df.to_csv(filename, index=False)
        print(f"Data exported to {filename}")
    
    def export_to_excel(self, filename="students.xlsx"):
        """Export data to Excel file"""
        try:
            import openpyxl
            df_export = self.df.copy()
            df_export["Average"] = df_export[self.SUBJECTS].mean(axis=1)
            df_export.to_excel(filename, index=False)
            print(f"Data exported to {filename}")
        except ImportError:
            print("openpyxl not installed. Cannot export to Excel.")
    
    def get_dataframe(self):
        """Get the underlying DataFrame"""
        return self.df
    
    def search_student(self, first_name=None, last_name=None):
        """Search for a student by name"""
        result = self.df.copy()
        
        if first_name:
            result = result[result["First Name"].str.contains(first_name, case=False)]
        if last_name:
            result = result[result["Last Name"].str.contains(last_name, case=False)]
        
        return result


def get_student_input():
    """Get student information from user input"""
    
    print("\n" + "-"*60)
    print("Enter Student Information")
    print("-"*60)
    
    first_name = input("First name: ").strip()
    last_name = input("Last name: ").strip()
    
    if not first_name or not last_name:
        print("Error: Name cannot be empty")
        return None, None, None
    
    print("\nEnter 5 grades (0-100):")
    grades = []
    subjects = StudentDataManager.SUBJECTS
    
    for idx, subject in enumerate(subjects):
        try:
            grade = float(input(f"  {idx + 1}. {subject}: "))
            if not (0 <= grade <= 100):
                raise ValueError
            grades.append(grade)
        except ValueError:
            print(f"Error: Invalid grade. Must be between 0 and 100")
            return None, None, None
    
    return first_name, last_name, grades


# Main program
# Create data directory if it doesn't exist
data_dir = Path("/home/crispri/Study/praktyka 1 rozdil/tasks/data")
data_dir.mkdir(exist_ok=True)

csv_file = data_dir / "students.csv"

# Initialize manager
manager = StudentDataManager(str(csv_file))

# Add sample data if the file is empty
if manager.df.empty:
    print("\nAdding sample students...")
    
    sample_data = [
        ("Ivan", "Petrov", [85, 90, 78, 88, 92]),
        ("Maria", "Sidorenko", [92, 88, 95, 90, 87]),
        ("Oleh", "Kovalenko", [78, 75, 80, 82, 79]),
        ("Natalia", "Bondarenko", [88, 92, 89, 91, 90]),
        ("Dmytro", "Shevchenko", [72, 68, 75, 70, 74]),
        ("Kateryna", "Levcenko", [95, 93, 96, 94, 95]),
    ]
    
    for first_name, last_name, grades in sample_data:
        manager.add_student(first_name, last_name, grades)
    
    manager.save_data()
    print(f"Sample data saved to {csv_file}")

# Display initial data
manager.display_table()
manager.display_subject_statistics()
manager.display_ranking()

# Interactive mode
while True:
    print("\n" + "-"*60)
    print("Menu:")
    print("  1. Add new student")
    print("  2. Remove student")
    print("  3. Display all students")
    print("  4. Show subject statistics")
    print("  5. Show student ranking")
    print("  6. Search student")
    print("  7. Export to Excel")
    print("  8. Show raw DataFrame info")
    print("  9. Save and exit")
    print("  0. Exit without saving")
    print("-"*60)
    
    choice = input("\nChoose option (0-9): ").strip()
    
    if choice == '1':
        first_name, last_name, grades = get_student_input()
        if first_name:
            if manager.add_student(first_name, last_name, grades):
                print(f"Student {first_name} {last_name} added successfully!")
                manager.save_data()
    
    elif choice == '2':
        print("\nCurrent students:")
        df_display = manager.df[["First Name", "Last Name"]].copy()
        print(df_display.to_string(index=True))
        
        try:
            print("\nEnter student number to remove or 'cancel' to go back:")
            remove_input = input("Student number: ").strip()
            if remove_input.lower() == 'cancel':
                continue
            
            remove_idx = int(remove_input)
            if 0 <= remove_idx < len(manager.df):
                first = manager.df.iloc[remove_idx]["First Name"]
                last = manager.df.iloc[remove_idx]["Last Name"]
                manager.remove_student(first, last)
                manager.save_data()
            else:
                print("Invalid student number")
        except ValueError:
            print("Invalid input")
    
    elif choice == '3':
        manager.display_table()
    
    elif choice == '4':
        manager.display_subject_statistics()
    
    elif choice == '5':
        manager.display_ranking()
    
    elif choice == '6':
        search_name = input("\nEnter part of student name to search: ").strip()
        if search_name:
            results = manager.search_student(first_name=search_name)
            if results.empty:
                results = manager.search_student(last_name=search_name)
            
            if not results.empty:
                print(f"\nFound {len(results)} student(s):")
                print(results.to_string(index=False))
            else:
                print("No students found")
    
    elif choice == '7':
        excel_file = data_dir / "students.xlsx"
        manager.export_to_excel(str(excel_file))
    
    elif choice == '8':
        print("\nDataFrame Info:")
        print(manager.df.info())
        print("\nDataFrame Description:")
        print(manager.df.describe())
    
    elif choice == '9':
        manager.save_data()
        print("Data saved. Exiting...")
        break
    
    elif choice == '0':
        print("Exiting without saving...")
        break
    
    else:
        print("Invalid choice. Please try again.")