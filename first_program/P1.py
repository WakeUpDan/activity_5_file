class FileProcessor:
    def __init__(self, input_file):
        self.input_file = input_file
        self.numbers = []
    
    def load_numbers(self):
        """Reads numbers and populates the numbers list."""
        try:
            with open(self.input_file, 'r') as f:
                for line in f:
                    clean_line = line.strip()
                    if clean_line:
                        # Converting to float first handles cases like '12.0' 
                        # then to int for clean parity checking
                        self.numbers.append(int(float(clean_line)))
            return True
        except FileNotFoundError:
            print(f"Error: {self.input_file} not found.")
            return False
        except ValueError as e:
            print(f"Error: Found non-numeric data. {e}")
            return False
    
class NumberSorter:
    def __init__(self, data):
        self.data = data
        self.evens = []
        self.odds = []
    
    def sort(self):
        for n in self.data:
            if n % 2 == 0:
                self.evens.append(n)
            else:
                self.odds.append(n)

    def save(self, even_file, odd_file):
        """Saves the sorted results to respective files."""
        try:
            with open(even_file, 'w') as fe:
                fe.write("\n".join(map(str, self.evens)) + "\n")
            with open(odd_file, 'w') as fo:
                fo.write("\n".join(map(str, self.odds)) + "\n")
            return True
        except IOError as e:
            print(f"File writing error: {e}")
            return False
