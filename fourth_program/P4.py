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
        if not self.data:
            print("No data to process.")
            return
        
        # Example processing: Calculate squares of the integers
        processed_data = [str(num ** 2) for num in self.data]
        
        output_file = "processed_integers.txt"
        try:
            with open(output_file, 'w') as f:
                f.write("\n".join(processed_data))
            print(f"Processed data saved to {output_file}.")
        except IOError as e:
            print(f"An error occurred while writing to file: {e}")