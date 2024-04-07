questions = """


"""

questions_list = questions.strip().split("\n")

def getQuestion(index):
    index-=1
    print("\n",questions_list[index], "\n")
    

def main():
    while True:
        choice = int(input("Enter a question number or enter \033[31m 0 \033[0m to Quit : "))
        if choice == 0:
            print("Quitting...")
            break;
        else :
            getQuestion(choice)
            if choice == 1:
                print(choice)
            else:
                print("Invalid Input. Please Retry...")
                
if __name__ == "__main__":
    main()