import os
import numpy as np

questions = """
1. Demonstrate random integer & random float.

2. Demonstrate 1-D & 2-D random arrays.

3. Generate random number from 1-D & 2-D random arrays.

4. Generate a 1-D & 2-D random arrays, containing 25 values, where each value has to be 5, 10, 15 or 20.

5. Generate a random permutation of elements of a random array.
"""

question_list = questions.strip().split("\n\n")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_question(index):
    index-=1
    print(f"\n\033[33m{question_list[index]}\033[0m\n")

def question1():
    integer = np.random.randint(1,5)
    decimel = round(np.random.uniform(5, 10), 2)

    print(f"Random Integer [randint()] : {integer}\nRandom Float [uniform()] : {decimel}")

def question2():
    one_d_integer_array = np.random.randint(1, 20, size=10)
    two_d_integer_array = np.random.rand(2,5)
    print(f"1-D array [randint()] : {one_d_integer_array}\n\n2-D array [rand()] : {two_d_integer_array}")

def question3():
    one_d_integer_array = np.random.randint(1, 20, size=10)
    two_d_integer_array = np.round(np.random.rand(2,5), 2) * 100 # just to round 1 place
    print(f"1-D array : {one_d_integer_array}\n\n2-D array : {two_d_integer_array}\n")
    ond_d_choice = np.random.choice(one_d_integer_array)
    two_d_choice = np.random.choice(two_d_integer_array.flatten())
    print(f"1-D array choice [randint() -> choice()] : {ond_d_choice}\n\n2-D array choice [round(){{just for fun}} -> rand() -> flatten(){{without flattening the multi-dimensional array we can't pick a value -> choice()}}] : {two_d_choice}")


def question4():
    values = [5,10,15,20]

    integer_array = np.random.choice(values, size=25)
    decimel_array = np.random.choice(values, size=(5,5))

    print(f"1-D array with 25 elements: {integer_array}\n\n2-D array with 25 elements: {decimel_array}")


def question5():
    integer_array = np.random.randint(2, 20, size=10)
    print(f"1-D array with 25 elements: {integer_array}\n")
    
    random_permutations = np.random.permutation(integer_array)
    print(f"Random permutations from a generated-random-array : {random_permutations}")

def main():
    while True:
        try:
            print(f"\033[32mTopics covered - [numpy.random(), randint(), rand(), uniform(), choice(), permutations()]\033[0m")
            choice = input("Enter a question number \033[36m[1 - 5]\033[0m \033[33mor\033[0m\nenter \033[31m ↵ \033[0m to clear console\nenter \033[31m 0 \033[0m to Quit : ")
            if(choice == ""):
                clear_console()
            else:
                choice = int(choice)
                if choice == 0:
                    print("Quitting...")
                    break;
                elif 0 < choice <= 5 :
                    clear_console()
                    get_question(choice)
                    if choice == 1:
                        question1()
                        print("\n")
                    elif choice == 2:
                        question2()
                        print("\n")
                    elif choice == 3:
                        #print(f"choice = {choice}")
                        question3()
                        print("\n")
                    elif choice == 4:
                        question4()
                        print("\n")
                    elif choice == 5:
                        question5()
                        print("\n")
                    else:
                        print("Invalid Input. Enter questions from 1 to 5")

        except ValueError:
            print("Invalid Input. Please Retry...")

if __name__ == "__main__":
    main()