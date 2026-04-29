class IntegerProcessor:
    def __init__(self, source_file):
        self.source_file = source_file
        self.integers = []

    def read_integers(self):
        """Reads integers from the source file."""
        try:
            with open(self.source_file, 'r') as file:
                # Convert each line to an integer and store in a list
                self.integers = [int(line.strip()) for line in file if line.strip()]
        except FileNotFoundError:
            print(f"Error: '{self.source_file}' was not found.")
        except ValueError:
            print("Error: Ensure the file contains only integers (one per line).")

    def process_and_save(self):
        """Calculates square for evens and cube for odds, then saves to files."""
        if not self.integers:
            print("No data to process.")
            return

        try:
            # Open both output files at once
            with open("double.txt", "w") as even_file, \
                 open("triple.txt", "w") as odd_file:
                
                for num in self.integers:
                    if num % 2 == 0:
                        # Even logic: Square it
                        even_file.write(f"{num ** 2}\n")
                    else:
                        # Odd logic: Cube it
                        odd_file.write(f"{num ** 3}\n")
            
            print("Success! 'double.txt' and 'triple.txt' have been updated.")
            
        except IOError as e:
            print(f"An error occurred while writing: {e}")

# Main execution block
if __name__ == "__main__":
    # 1. Create the processor instance
    processor = IntegerProcessor("integers.txt")
    
    # 2. Read the source file
    processor.read_integers()
    
    # 3. Process and create output files
    processor.process_and_save()