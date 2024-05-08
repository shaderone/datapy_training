import pandas as pd
import string as st

questions = """
1. Create a pandas series from a list of first 20 even numbers.

2. Print the first & last elements of the above generated series.

3. Change the label of the above generated pandas series to capital letter alphabets.

4. Create a pandas series from a dictionary, containing first 10 odd numbers as values.

5. Create a data frame from two series, where one series is sqaures of first 10 integers & the second series is cubes of first 10 integers.

6. Create a pandas dataframe & demonstrate the following operations.
a. loc
b. index changing
c. use loc after index changing

"""
#----------------------------------------------------------

questions_list = questions.strip().split("\n\n")

def getQuestion(choice):
    choice -= 1
    print(f'\n{questions_list[choice]}\n')

#----------------------------------------------------------

#? common for question 1,2,3 
even_num_list = [i for i in range(2,20+1,2)]
series_from_list = pd.Series(even_num_list)

#? common for question 3,6 
def get_alphabet_index(limit):
    return list(st.ascii_lowercase[:limit])

#? common for question 5 and 6
squares_series = pd.Series([x ** 2 for x in range(1, 11)])
cubes_series = pd.Series([x ** 3 for x in range(1, 11)])
data_frame_from_series = pd.DataFrame({"squares" : squares_series, "cubes": cubes_series})

def question1():
    print(series_from_list)

def question2():
    print(f'Top -> {series_from_list.head(1).values} | Bottom -> {series_from_list.tail(1).values}')

def question3():
    series_from_list.index = (get_alphabet_index(len(series_from_list)))
    print(series_from_list)

def question4():
    odd_num_list = [i for i in range(1,20,2)]
    odd_dict = {index : value for index, value in enumerate(odd_num_list)}
    series_from_dictionary = pd.Series(odd_dict)
    print(series_from_dictionary)

def question5():
    print(data_frame_from_series)

def question6():
    print(f"-> loc[0]")
    print(data_frame_from_series.loc[0])
    print(f"\n-> index changing")
    data_frame_from_series.set_index(pd.Index(get_alphabet_index(len(data_frame_from_series))), inplace=True)
    print(data_frame_from_series)
    print(f"\n-> loc['a'] after index change")
    print(data_frame_from_series.loc["a"])
    # Resetting the index back to default integer index
    data_frame_from_series.reset_index(drop=True, inplace=True)

def main():
    while True:
        try:
            choice = int(input("Enter a question number or enter \033[31m 0 \033[0m to Quit : "))
            if choice == 0:
                print("Quitting...")
                break;
            elif 0 < choice < 7 :
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
                    question4()
                    print("\n")
                elif choice == 5:
                    question5()
                    print("\n")
                elif choice == 6:
                    question6()
                    print("\n")
            else :
                print("Invalid Input. Please Retry...")

        except ValueError:
            print("Invalid Input. Please Retry...")
            
if __name__ == "__main__":
    main()