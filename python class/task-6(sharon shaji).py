import user_module as um
import os

questions = """

1. Create a module which contains functions for calculating prime number, factoarial, fibonacci series, armstrong number, sun of 'n' numbers under "user_module.py" and use it as a library in another python program and demonstrate all functions.

2. Create a sample text file containing the following text & demonstrate open & read file handling operations
Text :
Hi...
Good Morning.
Welcome to Python.

3. Demonstrate all the file handling operations in detail, while using all the attributes.

"""

questions_list = [item.strip() for item in questions.split("\n\n") if item.strip()]
COLOR1_START = "\033[32m"
COLOR1_END = "\033[0m"
COLOR2_START = "\033[33m"
COLOR2_END = "\033[0m"

def getQuestion(index):
    index-=1
    print("\n",questions_list[index],"\n")
    

class FileHandler:
    def __init__(self, file_name):
        self.filename = file_name

    def create_file(self):
        print(f"{COLOR2_START}-> creating / opening file ...{COLOR2_END}")
        with open(self.filename, "w") as file:
            file.write("Hi...\nGood Morning.\nWelcome to Python.")
        print("content added! closing...\n")

    def open_file(self):
        print(f"{COLOR2_START}-> opening and reading file content ...{COLOR2_END}")
        with open(self.filename, "r") as file:
            content = file.read()
            print(f"{COLOR1_START}{content}{COLOR1_END}")

class FileOperations(FileHandler):
    def __init__(self,file_name):
        super().__init__(file_name)

    def append_to_file(self, text):
        """Add content without overwriting"""
        print(f"{COLOR2_START}\n-> opening and adding content ...{COLOR2_END}\n{text}")
        with open(self.filename, "a") as file:
            file.write("\n" + text)

    def read_line_by_line(self):
        print(f"{COLOR2_START}\n-> opening and reading content line by line ...{COLOR2_END}")
        with open(self.filename, "r") as file:
            for line in file:
                print(f"{COLOR1_START}{line.strip()}{COLOR1_END}")

    def rename_file(self, new_filename):
        print(f"{COLOR2_START}\n-> Renaming file ...{COLOR2_END}")
        os.rename(self.filename, new_filename)
        self.filename = new_filename
        print(f"File renamed from {self.filename} to '{new_filename}'.")

    def delete_file(self):
        print(f"{COLOR2_START}\n-> Deleting file ...{COLOR2_END}")
        os.remove(self.filename)
        print(f"File '{self.filename}' deleted.")

def main():
    while True:
        try:
            choice = int(input("Enter a question number or enter \033[31m 0 \033[0m to Quit : "))
            if choice == 0:
                print("Quitting...")
                break;
            elif 0 < choice <= 3 :
                getQuestion(choice)
                if choice == 1:
                    try:
                        print(f"prime check for 23 & 15: {COLOR1_START}{um.check_prime(23)} & {um.check_prime(15)}{COLOR1_END}")
                        print(f"Factorial of 5 : {COLOR1_START}{um.get_factorial(5)}{COLOR1_END}")
                        print(f"Fibonacci of 10 : {COLOR1_START}{um.get_fibonacci(10)}{COLOR1_END}")
                        print(f"Amstrong check for 153 & 11: {COLOR1_START}{um.check_armstrong(153)} & {um.check_armstrong(11)}{COLOR1_END}")
                        print(f"Getting sum of numbers till 10 : {COLOR1_START}{um.get_sum(3)}{COLOR1_END}")
                    except um.IncorrectInputException as e:
                        print(e)
                    print("\n")
                elif choice == 2:
                    fh = FileHandler("test.txt")
                    fh.create_file()
                    fh.open_file()
                    print("\n")
                elif choice == 3:
                    file = FileOperations("test.txt")
                    file.create_file()
                    file.open_file()
                    file.append_to_file("\nFact: Python got its name from a TV series")
                    file.read_line_by_line()
                    file.rename_file("new_test.txt")
                    file.delete_file()
                    print("\n")
            else :
                print("Invalid Input. Please Retry...")

        except ValueError:
            print("Invalid Input. Please Retry...")
            
if __name__ == "__main__":
    main()