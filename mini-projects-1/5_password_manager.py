from cryptography.fernet import Fernet
from InquirerPy import inquirer, prompt
import _helper as hp

#def generate_key():
#    key = Fernet.generate_key()
#    with open('key.key','wb') as key_file:
#        key_file.write(key)
#generate_key()

def load_key():
    with open('key.key','rb') as key_file:
        key = key_file.read()
    return key

def view(fernet):
    try:
        with open('passwords.txt','r') as file:
            #loop through each line
            for line in file.readlines():
                data = line.rstrip()
                name, password = data.split("|")
                decrypted_password = fernet.decrypt(password.encode()).decode()
                print(f"user : {name}, password : {decrypted_password}")
    except FileNotFoundError:
        print("No accounts exist!")

def add(fernet):
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

    encrypted_password = fernet.encrypt(password.encode()).decode()
    with open('passwords.txt','a') as file:
        file.write(f'{name} | {encrypted_password}\n')
    
    print("New password stored\n")

def main():
    #master_password = input("Enter the master password: ").encode()
    
    key = load_key() 
    fernet = Fernet(key)
    
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
            view(fernet)
        elif choice == "Store New Password":
            add(fernet)

    

if __name__ == "__main__":
    main()