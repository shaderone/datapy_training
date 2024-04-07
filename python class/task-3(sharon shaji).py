def getQuestion(index, questions_list):
    index -= 1
    print("\n", questions_list[index], "\n")

def question_1(number):
    fact = 1
    for i in range(1, number + 1):
        fact *= i

    fact = 1 if number == 0 else fact
    print(f"factorial of {number} = {fact}\n")

def question_2(string):
    lower_case_count = 0
    upper_case_count = 0
    for char in string:
        if char.islower():
            lower_case_count += 1
        elif char.isupper():
            upper_case_count += 1
    print(f"{string} has {upper_case_count} uppercase, {lower_case_count} lowercase letters in it\n")

def question_3(string):
    print("input: ", string)
    res = "-".join(sorted(string.split("-")))
    print("result: ", res, "\n")

def question_4(numbers):
    square = lambda number: number ** 2
    squared_number = [square(number) for number in numbers]
    cube = lambda number: number ** 3
    cubed_number = [cube(number) for number in numbers]
    print(f"Values = {numbers}")
    print(f"square - {squared_number}, cube - {cubed_number}\n")

def question_5(string, key):
    if string.startswith(key):
        print(f"{string} \033[33mSTARTS\33[0m with {key}\n")
    else:
        print(f"{string} \033[33mDOES NOT START\33[0m with {key}\n")

def main():
    questions = """
1. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
2. Write a Python function that accepts a string and calculates the number of uppercase letters and lowercase letters.
3. Write a Python function that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
4. Write a Python program to square and cube every number in a given list of integers using Lambda.
5. Write a Python program to find if a given string starts with a given character using Lambda.
    """

    questions_list = questions.strip().split("\n")
    while True:
        try:
            choice = int(input("\n\033[36mEnter a question number or enter\033[0m \033[31m0\033[0m \033[36mto Quit\33[0m : "))
            if choice == 0:
                print("Quitting...")
                break

            elif 0 < choice <= 5:
                getQuestion(choice, questions_list)
                if choice == 1:
                    value = input("Press \033[33m ↵ \033[0m to use the default value or Enter a number : ")
                    value = 5 if value == "" else int(value)
                    question_1(value)

                elif choice == 2:
                    value = input("Press \033[33m ↵ \033[0m to use the default value or Enter a string: ")
                    value = "StRing" if value == "" else value
                    question_2(value)

                elif choice == 3:
                    value = input("Press \033[33m ↵ \033[0m to use the default value or Enter hyphen-separated words: ")
                    value = "test-my-driving-to-the-limit" if value == "" else value
                    question_3(value)

                elif choice == 4:
                    value = input("Press \033[33m ↵ \033[0m to use the default value or Enter a limit : ")
                    value = [int(num) for num in "1,2,3,4,5".split(",")] if value == "" else list(map(int, input("Enter numbers separated by comma: ").split(",")))
                    question_4(value)

                elif choice == 5:
                    string_value = input("Press \033[33m ↵ \033[0m to use the default value or Enter a string: ")
                    key_value = input("Enter the character to look for in the string: ")
                    string_value = "hello world" if string_value == "" else string_value
                    key_value = "w" if key_value == "" else key_value
                    question_5(string_value, key_value)

            else:
                print("Invalid Input. Please Retry...")

        except ValueError:
            print("Invalid Input. Please Retry...")

if __name__ == "__main__":
    main()
