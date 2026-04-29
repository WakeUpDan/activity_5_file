class Student:
    """Class to model the student entity."""
    def __init__(self, name, gwa):
        self.name = name.strip()
        self.gwa = float(gwa)
    def __repr__(self):
        return f"{self.name} | GWA: {self.gwa:.2f}"

class FileProcessor:
    """Handles all file-related operations."""
    def __init__(self, filename):
        self.filename = filename

    def read_students_data(self):
        """Reads student data from the file."""
        students = []
        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    name, gwa = line.strip().split(',')
                    students.append(Student(name, gwa))
                return students
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
        except ValueError:
            print("Error: Invalid data format in the file.")
        return students

class GradeAnalyzer:
    """Contains logic for analyzing student performance."""
    def __init__(self, students):
        self.students = students

    def find_top_performer(self):
        """Returns the student with the best GWA (lowest numerical value)."""
        if not self.students:
            return None
        # Using min() because 1.00 < 5.00 in the PH grading scale
        return min(self.students, key=lambda s: s.gwa)

def main():
    # 1. Initialize File Handler
    file_manager = FileProcessor("students.txt")
    
    # 2. Extract Data
    data = file_manager.read_students_data()
    
    # 3. Analyze Data
    analyzer = GradeAnalyzer(data)
    top_student = analyzer.find_top_performer()
    
    # 4. Display Results
    print("=" * 35)
    print("    GWA LEADERBOARD RESULT")
    print("=" * 35)
    if top_student:
        print(f"TOP STUDENT: {top_student.name}")
        print(f"GWA:         {top_student.gwa:.2f}")
    else:
        print("No valid student records processed.")
    print("=" * 35)

if __name__ == "__main__":
    main()
