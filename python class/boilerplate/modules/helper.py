import subprocess as prs
import os
import sys
from modules import data

import socket

questions = """
1. Check the matplotlib version

2. Draw a line in a diagram from position (0, 0) to position (5, 250) using pyplot. Given (x, y) coordinates.

3. Draw a line in a diagram from position (0, 250) to position (0, 0) using pyplot. Given (x, y) coordinates.

4. Draw a line in a diagram from position (1, 5) to (2, 10) then to (3, 3) then to (4, 8) and finally to position (5, 0). Given (x, y) coordinates.

5. For the above plotted diagram, try the following markers.
a. 'o'
b. '*'
c. '.'
d. 'X'
e. '+'

6. For the plotted diagram in question 4, try the following line references.
a. '-'
b. ':'
c. '--'
d. '-.'

7. For the plotted diagram in question 4, try the following colour references.
a. 'r'
b. 'g'
c. 'b'
d. 'c'
e. 'm'
f. 'y'
g. 'k'
h. 'w'

8. For the plotted diagram in question 4, create the labels for X & Y axes, and also create a title for the same.

9. For the plotted diagram in question 4, add grid lines.
"""
questions_list = questions.strip().split("\n\n")

def getQuestion(index):
    index-=1
    print("\n",questions_list[index])

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def install_requirements():
    requirements = [
        "numpy",
        "pandas",
        "matplotlib",
    ]
    try:
        socket.create_connection(("8.8.8.8", 53)) #Testing for network connectivity
        prs.check_call(['pip', 'install'] + requirements)
    except prs.CalledProcessError:
        print("Invalid requirement mentioned")
    except OSError:
        print("\033[91mError: Not connected to the internet.\033[0m")
        sys.exit(1)

    #clear_console()

install_requirements()

def check_packages():
    try:
        import numpy
        import pandas 
        import matplotlib
    except (ImportError, ModuleNotFoundError) :
        install_requirements()
        #clear_console()

def make_files():
    check_packages()
    import pandas as pd
    global df_csv, df_excel
    df_csv = pd.DataFrame(data.car_data, columns=data.car_data[0])
    df_csv.to_csv('car_csv.csv', index=False)
    df_excel = pd.DataFrame(data.population_data, columns=data.population_data[0])
    df_excel.to_excel('population_excel.xlsx', index=False)

make_files()

def print_files(file_type=""):
    if(file_type == "" or file_type == None):
        print(df_csv.to_string())
        print()
        print(df_excel.to_string())
    elif(file_type.lower() == 'c'):
        print(df_csv.to_string())
    elif(file_type.lower() == 'e'):
        print(df_excel.to_string())

    print()

print_files()