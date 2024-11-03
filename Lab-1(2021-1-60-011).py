import random

class File:
    def __init__(self, filename):
        self.filename = filename

    def get_roll(self):
        numbers = []
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    cleaned_line = line.strip()
                    if cleaned_line.isdigit():
                        numbers.append(int(cleaned_line))
                    elif self._is_valid_roll(cleaned_line):
                        numbers.append(float(cleaned_line))
        except FileNotFoundError:
            print(f"Error: The file '{self.filename}' does not exist.")
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
        return numbers

    def _is_valid_roll(self, text):
        try:
            float(text)
            return True
        except ValueError:
            return False


class RandomRoll:
    def __init__(self, data):
        self.data = data

    def pick_one(self):
        if not self.data:
            print("The list is empty, nothing to pick.")
            return None
        return random.choice(self.data)



if __name__ == "__main__":
    file_name = "roll.txt"  

    
    file_handler = File(file_name)
    number_list = file_handler.get_roll()

   
    random_picker = RandomRoll(number_list)
    selected_roll = random_picker.pick_one()

    if selected_roll is not None:
        print(f"The Randomly selected Roll is: {selected_roll}")
