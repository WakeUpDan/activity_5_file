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

