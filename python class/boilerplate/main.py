from modules import helper

def main():
    while True:
        try:
            choice = int(input("Enter a question number or enter \033[31m 0 \033[0m to Quit : "))
            if choice == 0:
                print("Quitting...")
                break;
            elif 0 < choice <= 9 :
                helper.getQuestion(choice)
                if choice == 1:
                    print("\n")
                elif choice == 2:
                    print("\n")
                elif choice == 3:
                    print("\n")
                elif choice == 4:
                    print("\n")
                elif choice == 5:
                    print("\n")
                elif choice == 6:
                    print("\n")
                elif choice == 7:
                    print("\n")
                elif choice == 8:
                    print("\n")
                elif choice == 9:
                    print("\n")
            else :
                print("Invalid Input. Please Retry...")

        except ValueError:
            print("Invalid Input. Please Retry...")
            
if __name__ == "__main__":
    main()