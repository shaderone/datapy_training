from modules import helper
import matplotlib as mpl
import matplotlib.pyplot as plt

def question1():
    print("Matplotlib version:", mpl.__version__)

def question2():
    x1, y1 = 0,0
    x2, y2 = 5, 250

    plt.plot([x1,x2], [y1,y2])

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Line Plot with Starting and Ending Coordinates')

    plt.grid(True)
    plt.show()

def question3():
    x1, y1 = 0,250
    x2, y2 = 0, 0

    plt.plot([x1,x2], [y1,y2])

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Line Plot with Starting and Ending Coordinates')

    plt.xlim(-5, 5)
    plt.ylim(0, 300)

    plt.grid(True)
    plt.show()

def question4():
    x_coords = [1, 2, 3, 4, 5]
    y_coords = [5, 10, 3, 8, 0]

    plt.plot(x_coords, y_coords)

    plt.xlabel('X - axis')
    plt.ylabel('Y - axis')
    plt.title('Line from (1, 5) to (2, 10) to (3, 3) to (4, 8) to (5, 0)')

    plt.show()

def question5(marker):
    x_coords = [1, 2, 3, 4, 5]
    y_coords = [5, 10, 3, 8, 0]

    plt.plot(x_coords, y_coords, marker=marker)

    plt.xlabel('X - axis')
    plt.ylabel('Y - axis')
    plt.title('Line from (1, 5) to (2, 10) to (3, 3) to (4, 8) to (5, 0)')

    plt.show()

def question6(line_ref, label):
    x_coords = [1, 2, 3, 4, 5]
    y_coords = [5, 10, 3, 8, 0]

    plt.plot(x_coords, y_coords, linestyle=line_ref, marker='o', label=label)

    plt.xlabel('X - axis')
    plt.ylabel('Y - axis')
    plt.title('Line from (1, 5) to (2, 10) to (3, 3) to (4, 8) to (5, 0)')

    plt.legend()
    plt.show()

def question7(color,label, title='Line from (1, 5) to (2, 10) to (3, 3) to (4, 8) to (5, 0)'):
    x_coords = [1, 2, 3, 4, 5]
    y_coords = [5, 10, 3, 8, 0]

    plt.plot(x_coords, y_coords, color=color, marker='o', label=label)

    plt.xlabel('X - axis')
    plt.ylabel('Y - axis')
    plt.title(title)

    plt.legend()
    plt.grid(True)
    plt.show()


def question8():
    question7('r','red', title="With Labels and Title")

def question9():
    question7('g','green', title="With Grid lines")


def main():
    while True:
        try:
            choice = input("Enter a question number \033[36m[1 - 9]\033[0m \033[33mor\033[0m\nenter \033[31m ↵ \033[0m to clear console\nenter \033[31m 0 \033[0m to Quit : ")
            if(choice == ""):
                helper.clear_console()
            else:
                choice = int(choice)
                if choice == 0:
                    print("Quitting...")
                    break;
                elif 0 < choice <= 9 :
                    helper.getQuestion(choice)
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
                        marker_labels = {
                            'o': 'Circle',
                            '*': 'Star',
                            '.': 'Point',
                            'X': 'Cross',
                            '+': 'Plus'
                        }
                        while True:
                            try:
                                marker_choice = input("->\tSelect a marker type \033[36m['o', '*', '.', 'X','+']\033[0m \033[33mor\033[0m\n\tenter \033[31m ↵ \033[0m to clear console \033[33mor\033[0m\n\tenter \033[31m e \033[0m to Exit question : ")
                                
                                if(marker_choice == ""):
                                    helper.clear_console()
                                else:
                                    if marker_choice == 'e':
                                        print("Going back...")
                                        break;
                                    elif marker_choice in marker_labels.keys():
                                        question5(marker=marker_choice)
                                        print("\n")
                                    else :
                                        print("Invalid Input. Please Retry...")

                            except ValueError:
                                print("Invalid Input. Please Retry...")

                    elif choice == 6:
                        line_styles = {
                            '-': 'solid',
                            ':': 'dotted',
                            '--': 'dashed',
                            '-.': 'dashdot'
                        }
                        while True:
                            try:
                                line_ref_choice = input("->\tSelect a marker type \033[36m['-', ':', '--', '-.']\033[0m \033[33mor\033[0m\n\tenter \033[31m ↵ \033[0m to clear console \033[33mor\033[0m\n\tenter \033[31m e \033[0m to Exit question : ").strip()

                                if(line_ref_choice == ""):
                                    helper.clear_console()
                                else:
                                    if line_ref_choice == 'e':
                                        print("Going back...")
                                        break;
                                    elif line_ref_choice in line_styles.keys():
                                        question6(line_ref=line_ref_choice, label=line_styles[line_ref_choice])
                                        print("\n")
                                    else :
                                        print("Invalid Input. Please Retry...")

                            except ValueError:
                                print("Invalid Input. Please Retry...")

                    elif choice == 7:
                        line_colors = {
                            'r': 'red',
                            'g': 'green',
                            'b': 'blue',
                            'c': 'cyan',
                            'm': 'magenta',
                            'y': 'yellow',
                            'k': 'black',
                            'w': 'white'
                        }

                        while True:
                            try:
                                color_choice = input("->\tSelect a marker type \033[36m['r', 'g', 'b', 'c', 'm', 'y', 'k', 'w']\033[0m \033[33mor\033[0m\n\tenter \033[31m ↵ \033[0m to clear console \033[33mor\033[0m\n\tenter \033[31m e \033[0m to Exit question : ").strip()

                                if(color_choice == ""):
                                    helper.clear_console()
                                else:
                                    if color_choice == 'e':
                                        print("Going back...")
                                        break;
                                    elif color_choice in line_colors.keys():
                                        question7(color=color_choice, label=line_colors[color_choice])
                                        print("\n")
                                    else :
                                        print("Invalid Input. Please Retry...")

                            except ValueError:
                                print("Invalid Input. Please Retry...")

                    elif choice == 8:
                        question8()
                        print("\n")
                    elif choice == 9:
                        question9()
                        print("\n")
                else :
                    print("Invalid Input. Please Retry...")

        except ValueError:
            print("Invalid Input. Please Retry...")
            
if __name__ == "__main__":
    main()