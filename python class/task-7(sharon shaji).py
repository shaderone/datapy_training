import numpy as np
questions = """

1. Create a filter array that will return only even elements from the original array, using numpy.

2. Create 0-D, 1-D, 2-D & 3-D arrays using numpy & demonstrate the following.
a. Print the arrays
b. ndim
c. ndmin

3. Create a numpy array with 6 dimensions and verify that it has 6 dimensions.

"""

questions_list = questions.strip().split("\n\n")

def getQuestion(index):
    index-=1
    print("\n",questions_list[index], "\n")
    

def question1():
    original_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    filter_array = original_array[original_array % 2 == 0]

    print("Original Array:", original_array)
    print("Filtered Array (Even elements):", filter_array)


def question2():
    zero_d_array = np.array(42)

    one_d_array = np.array([1, 2, 3, 4, 5])

    two_d_array = np.array([[1, 2, 3], [4, 5, 6]], ndmin=6)

    three_d_array = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

    print("0-D Array (Scalar):", zero_d_array)
    print("ndim:", zero_d_array.ndim)
    print("ndmin:", zero_d_array.ndim)

    print("\n1-D Array:", one_d_array)
    print("ndim:", one_d_array.ndim)
    print("ndmin:", one_d_array.ndim)

    print("\n2-D Array:", two_d_array)
    print("ndim:", two_d_array.ndim)
    print("ndmin:", two_d_array.ndim)
    print("\033[33mThis Dimension is manually assigned.\033[0m")

    print("\n3-D Array:", three_d_array)
    print("ndim:", three_d_array.ndim)
    print("ndmin:", three_d_array.ndim)             


def question3():
    six_dim_array = np.array([1, 2, 3], ndmin=6)
    print(six_dim_array)
    print("Dimensions of the 6-D Array:", six_dim_array.ndim)


def main():
    while True:
        try:
            choice = int(input("Enter a question number or enter \033[31m 0 \033[0m to Quit : "))
            if choice == 0:
                print("Quitting...")
                break;
            elif 0 < choice <= 4 :
                getQuestion(choice)
                if choice == 1:
                    question1()
                    print("\n")
                elif choice == 2:
                    question2()
                    print("\n")
                elif choice == 3:
                    question3()
                    print("\n")
                elif choice == 4:
                    print("\n")
            else :
                print("Invalid Input. Please Retry...")

        except ValueError:
            print("Invalid Input. Please Retry...")
            
if __name__ == "__main__":
    main()