import pandas as pd
import matplotlib.pyplot as plt

questions = """
1. Create a string of minimum 20 characters & get the characters of string from 10 to 15 using both positive and negative indexing.

2. Create a list of 10 names & numbers each and sort the list. Then, remove all the numbers from the sorted list.

3. Write a python program which asks for a year from the user & calculates, if this year is a leap year or not. Use all the leap year calculation logic.

4. Write a python program to display the multiplication table values from 1-10, line by line, using nested for loop.
eg.
1 2 3 4 5 6 7 8 9 10 
2 4 6 8 10 12 14 16 18 20

5. Write a python program that accepts a string, splits the string by spaces, prints it, then rejoins the splitted string by underscore(_) and prints it again.

6. Write a python program to find maximum of three numbers using Lambda

7. Create a file containing the following text & demonstrate all the file handling operations in detail.
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.
It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.

8. a) Download a CSV or EXCEL file from any source and add it to the code.
b) Demonstrate loc, head, tail, info functions.
c) Demonstrate all the data wrangling operations.
d) Plot the dataset as line graph and histogram.
e) Create the labels for the above two plots.
"""
questions_list = questions.strip().split("\n\n")

def get_question(index):
    index -= 1
    print(f'\n{questions_list[index]}\n')

def question1():
    string = "this is question 1 of today's exam"
    print(f"string - {string}\n")
    print(string[9:15])

def question2():
    names = "rojan, shanu, sharon, jeena, basil, harishankar, adithyan, eren, rick, ragnar"
    numbers = '1,2,3,4,5,6,7,8,9,10'
    name_list_sorted = sorted(names.split(", "))
    number_list_sorted = sorted([int(number) for number in numbers.split(",")])
    print(f"names : {name_list_sorted}\nnumbers : {number_list_sorted}\n")

    print(f"after removing a numbers from numbers list : {number_list_sorted.clear()}")

def question3(year):
    print(f"year - {year}")
    if(year % 4 == 0):
        print("Leap year")
    else:
        print("NOT leap year!")

def question4():
    for number in range(1,10+1):
        for number2 in range(1, 10+1):
            print(f'{number * number2:2} ', end="")
        print()

def question5(names_list):
    names = names_list.split(" ")
    print(f'list - {names}')
    joined_names = "_".join(names)
    print(f'\nlist after joining - {joined_names}')

#?Question6
#max_number = lambda numbers: [max(number) for number in numbers]
max_number = lambda numbers: max(numbers)

def question7():
    # Create a file and writing the text 
    with open('sample_file.txt', 'w') as file:
        file.write('''Lorem Ipsum is simply dummy text of the printing and typesetting industry.
    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.
    It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.''')

    #Open the file in read mode
    with open('sample_file.txt', 'r') as file:
        # Step 3: Reading from the file
        contents = file.read()
        print("Contents of the file:")
        print(contents)

    # Append additional text to the file
    with open('sample_file.txt', 'a') as file:
        file.write('\n\nAdditional text appended to the file.')

    # Close the file
    print("\nFile closed automatically after 'with' block.")


def question8():

    df_csv = pd.read_csv("exam/car.csv")
    print(f"LOC :\n{df_csv.loc[0]}\n")
    print(f"HEAD :\n{df_csv.head()}\n")
    print(f"TAIL :\n{df_csv.tail()}\n")
    print(f"INFO :\n")
    df_csv.info()

    #data wrangling - modifying data to our needs
    df_csv.drop_duplicates(inplace=True)

#   LINE
    plt.plot(df_csv['Mileage (miles)'],df_csv['Year'])
    plt.xlabel('Year')
    plt.ylabel('Price ($)')
    plt.title('Price ($) vs. Year')
    plt.show()
#
#    #HISTOGRAM
    plt.hist(df_csv['Mileage (miles)'], bins=10, color='skyblue', edgecolor='black')
    plt.xlabel('Mileage (miles)')
    plt.ylabel('Frequency')
    plt.title('Histogram of Mileage')
    plt.grid(True)
    plt.show()

def main():
    while True:
        choice = input("Enter a question number [1-8] or press enter to quit: ")
        #choice = 8 #!commented line
        if choice == "":
            #break;
            exit()
        elif int(choice) in range(1,10):
            get_question(int(choice))
            match(int(choice)):
                case 1: question1()
                case 2: question2()
                case 3: question3(2012)
                case 4: question4()
                case 5: question5("rojan shanu sharon jeena basil harishankar adithyan eren rick ragnar")
                case 6: print(f'max number in [1,2,3] is {max_number([1,2,3])}')
                case 7: question7()
                case 8: question8()
        else:
            print("invvalid input.")        
        print("\n")

if __name__ == "__main__":
    main()