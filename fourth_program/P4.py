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
    
    def process_and_save(self):
        """Process the integers and save the results to a new file."""
        try:
            with open("double.txt", "w") as f_double, open("triple.txt", "w") as f_triple:
                for num in self.data:
                    if num % 2 == 0:
                        # Square of even integers
                        result = num ** 2
                        f_double.write(f"{result}\n")
                    else:
                        # Cube of odd integers
                        result = num ** 3
                        f_triple.write(f"{result}\n")
            return True
        except IOError as e:
            print(f"An error occurred while saving files: {e}")
            return False

if __name__ == "__main__":
    processor = IntegerProcessor()
    if processor.load_data():
        processor.process_and_save()