class LifeRecorder:
    def __init__(self, filename="mylife.txt"):
        self.filename = filename

    def write_to_file(self):
        """Collects user input and writes each entry to its own line."""
        try:
            # Using 'w' to start fresh; use 'a' to append to an existing file
            with open(self.filename, "w") as file:
                print(f"--- Recording to {self.filename} ---")
                
                while True:
                    # 1. Get the content
                    line_content = input("Write your line: ").strip()
                    
                    # 2. Write to file with a newline separator
                    if line_content:  # Prevents saving empty lines
                        file.write(line_content + "\n")
                    
                    # 3. Check for continuation
                    choice = input("Add another line? (y/n): ").lower().strip()
                    
                    if choice == 'n':
                        print(f"\nClosing file. Data saved to {self.filename}.")
                        break
                    elif choice != 'y':
                        print("Unknown command. Continuing by default...")

        except IOError as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    recorder = LifeRecorder()
    recorder.write_to_file()