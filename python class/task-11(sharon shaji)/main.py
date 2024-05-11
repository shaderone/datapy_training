from task_11 import helper
helper.check_packages()

csv_old = helper.df_csv
excel_old = helper.df_excel

#a. Cleaning empty cells
def clean_empty_cells():
    print_files_before(csv_old=csv_old, excel_old=excel_old)
    csv_new = helper.df_csv.fillna('')
    excel_new = helper.df_excel.fillna('')
    print_files_after(csv_new=csv_new, excel_new=excel_new)
    print(f"\n\n\033[33mcleaned empty cells\033[0m")
    print("""
We could use either of the following methods :
1)dropna() [used here] : Drop rows with at least 2 non-null values
2)fillna() : Fill missing values with specified values or empty string
3)df.interpolate() : Interpolate missing values
""".strip())

#b. Cleaning incorrect format
def clean_incorrect_format():
    import pandas as pd
    print_files_before(csv_old=csv_old, excel_old=excel_old)
    csv_old['Year'] = pd.to_numeric(csv_old['Year'], errors='coerce')
    csv_new = csv_old['Year'] = csv_old['Year'].astype(float, errors='ignore')
    excel_old['GDP per capita ($)'] = pd.to_numeric(excel_old['GDP per capita ($)'], errors='coerce')
    excel_new = excel_old['GDP per capita ($)'] = excel_old['GDP per capita ($)'].astype(float, errors='ignore')
    print_files_after(csv_new=csv_new, excel_new=excel_new)
    print(f"\n\n\033[33mCleaned incorrect format - here we first made the column numeric, and also coerced any non numeric cell to 'NaN. Then we 'ignore' this cell as we convert it to float type\033[0m")
    print("""
We could use either of the following methods :
1)astype() [used here] : Convert data type of a column
2)using regex : Correct formatting using regular expressions
""".strip())

#c. Cleaning incorrect data
def clean_incorrect_data():
    print_files_before(csv_old=csv_old, excel_old=excel_old)
    csv_new = csv_old['Model'] = csv_old['Model'].map(lambda x: x.upper() if isinstance(x, str) else x)  
    excel_new = excel_old['Country'] = excel_old['Country'].map(lambda x: x.upper() if isinstance(x, str) else x)  
    print_files_after(csv_new=csv_new, excel_new=excel_new)
    print(f"\n\n\033[33mclean incorrect data\033[0m")
    print("""
We could use either of the following methods :
1)applymap()  : Apply functions element-wise
2)map() or apply() [used here] : Apply functions to specific columns 
""".strip())

#d. Removing duplicates
def remove_duplicates():
    print_files_before(csv_old=csv_old, excel_old=excel_old)
    csv_new = csv_old.drop_duplicates()
    excel_new = excel_old.drop_duplicates()
    print_files_after(csv_new=csv_new, excel_new=excel_new)
    print(f"\n\n\033[33mremove_duplicates\033[0m")

def print_files_before(csv_old, excel_old):
    print("\033[32m---------------Before correction---------------\033[0m")
    print(f"\n\033[35m[csv_file]\033[0m{csv_old}")
    print(f"\n\033[35m[excel_file]\033[0m{excel_old}")

def print_files_after(csv_new, excel_new):
    print("\n\033[32m---------------After Correction---------------\033[0m")
    print(f"\n\033[35m[csv_file]\033[0m{csv_new}")
    print(f"\n\033[35m[excel_file]\033[0m{excel_new}")

operation_mapping = {
    "a": clean_empty_cells,
    "b": clean_incorrect_format,
    "c": clean_incorrect_data,
    "d": remove_duplicates,
    "e": helper.clear_console,
}

def main():

    while True:
        try:
            print("\033[34m----------------------------------------------------------------------------\033[0m")
            helper.getQuestion(2)
            print("e. clear console\n\033[32m[Available Operations]\033[0m\n")
            choice = input("enter operation number or enter \033[31m x \033[0m to Quit : ")
            if choice.lower() == "x":
                print("Quitting...")
                break;
            elif choice.lower() in operation_mapping :
                operation_mapping[choice]()
            else :
                print("\033[31mInvalid Input. Please Retry...\033[0m")

        except ValueError:
            print("Invalid Input. Please Retry...")
#            
if __name__ == "__main__":
    main()