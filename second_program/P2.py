class Student:
    """Class to model the student entity."""
    def __init__(self, name, gwa):
        self.name = name.strip()
        self.gwa = float(gwa)
    def __repr__(self):
        return f"{self.name} | GWA: {self.gwa:.2f}"
