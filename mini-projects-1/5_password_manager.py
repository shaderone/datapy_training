from InquirerPy import inquirer, prompt
import _helper as hp

def view():
    with open('passwords.txt','r') as file:
        #loop through each line
        for line in file.readlines():
            print(line.rstrip())
        print()

def add():
    questions = [
        {
            'type': 'input',
            'name': 'name',
            'message': 'Account Name: ',
        },
        {
            'type': 'password',
            'name': 'password',
            'message': 'Password: ',
        },
    ]
    
    answers = prompt(questions)

    # Get the user's input for account name and password
    name = answers['name']
    password = answers['password']

    with open('passwords.txt','a') as file:
        file.write(f'{name} | {password}\n')
    
    print("New password stored\n")

def main():
    #master_password = input("Enter the master password: ")
    while True:
        manager_options = ["View Passwords", "Store New Password", "Clear Screen", "Exit"]
        choice = inquirer.select(
            message="Select an option:",
            qmark="#",
            amark="#",
            choices=manager_options,
        ).execute()

        print(f"You selected '{choice}'")

        if choice == "Exit":
            hp.clear_console()
            exit("Program Complete!")
        elif choice == "Clear Screen":
            hp.clear_console()
        elif choice == "View Passwords":
            view()
        elif choice == "Store New Password":
            add()

    

if __name__ == "__main__":
    main()