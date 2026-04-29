class LifeRecorder:
    def __init__(self, filename="mylife.txt"):
        self.filename = filename

    def write_to_file(self):
        """Method to collect user input and write multiple lines to a file."""
        try:
            # 'w' mode overwrites/creates the file; use 'a' if you want to append later
            with open(self.filename, "w") as file:
                while True:
                    # Get the line from the user
                    line_content = input("Enter line: ")
                    
                    # Write the line and a newline character
                    file.write(line_content + "\n")
                    
                    # Check if the user wants to continue
                    more_lines = input("Are there more lines y/n? ").lower()
                    
                    if more_lines == 'n':
                        print(f"\nData successfully saved to {self.filename}.")
                        break
                    elif more_lines != 'y':
                        print("Invalid input, but assuming 'yes' to continue...")
        
        except IOError as e:
            print(f"An error occurred while writing to the file: {e}")

# --- Execution ---
if __name__ == "__main__":
    # Instantiate the class
    recorder = LifeRecorder()
    
    # Call the method to start the process
    recorder.write_to_file()