class LifeRecorder:
    def __init__(self, filename="mylife.txt"):
        self.filename = filename

    def write_to_file(self):
        """Collects user input and writes each entry to its own line."""
        try:
            # Using 'w' to start fresh; use 'a' to append to an existing file
            with open(self.filename, "w") as file:
                print(f"--- Recording to {self.filename} ---")
                