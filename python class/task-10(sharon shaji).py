import pandas as pd

COLOR_START = "\033[33m"
COLOR_END = "\033[0m"

def main():
    try:
        #loading csv and excel into dataframes
        print("1. Load a csv file & an excel file into two seperate dataframes.")
        csv_data = pd.read_csv("python class\\_files\\population.csv")
        excel_data = pd.read_excel("python class\\_files\\urban_census.xlsx")

        #* to_string()
        print(f"{COLOR_START} CSV data =>{COLOR_END}\n{csv_data.to_string()}\n")
        print(f"{COLOR_START} Excel data =>{COLOR_END}\n{excel_data.to_string()}\n")

        
        print("""
2. Demonstrate the following operations on the above created dataframes.
a. to_string
b. head
c. tail
d. info
""")
        #* head()
        print(f"{COLOR_START}HEAD(5) CSV data =>{COLOR_END}\n{csv_data.head(5)}\n")
        print(f"{COLOR_START}HEAD(3) Excel data =>{COLOR_END}\n{excel_data.head(3)}\n")

        #* tail()
        print(f"{COLOR_START}Tail(5) CSV data =>{COLOR_END}\n{csv_data.tail(5)}\n")
        print(f"{COLOR_START}Tail(3) Excel data =>{COLOR_END}\n{excel_data.tail(3)}\n")

        #* info()
        print(f"{COLOR_START}info CSV data =>{COLOR_END}\n")
        csv_data.info()
        print(f"\n{COLOR_START}info Excel data =>{COLOR_END}\n")
        excel_data.info()

    except ValueError:
        print("Invalid Input. Please Retry...")
            
if __name__ == "__main__":
    main()