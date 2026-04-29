class IntegerProcessor:
    def __init__(self, input_file="integers.txt"):
        self.input_file = input_file
        self.data = []
    
    def load_data(self):
        """Reads the integers from the source file."""
        try:
            with open(self.input_file, 'r') as f:
                # Read each line, convert to int, and store in a list
                self.data = [int(line.strip()) for line in f if line.strip()]
            return True
        except FileNotFoundError:
            print(f"Error: {self.input_file} not found.")
            return False
        except ValueError:
            print("Error: The file contains non-integer data.")
            return False