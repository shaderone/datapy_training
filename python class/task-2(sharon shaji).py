questions = """
1. Create a string & demonstrate the following.
2. Create a list & demonstrate the following.
3. Create a tuple & demonstrate the following.
4. Create a dictionary & demonstrate the following.
5. Briefly demonstrate the following categories of operators
6. Get the name & nationality of the user from the following
7. Display the first 11 natural numbers using while loop.
8. Create a list of n numbers, & reverse the list using loop.
9. Create a program to reverse the digits of given integer.
10. Create a program to print the below mentioned pattern.
11. Create a program to print the below mentioned pattern.
   
""";

questions_list = questions.strip().split('\n')

def getQuestion(index):
    index-=1
    print("\n",questions_list[index], "\n")

def question1():
    string = "The quick brown fox jumps 0ver the lazy dog!"
    string_with_tab = "The quick brown fox\tjumps over the lazy dog!"
    string_format = "The quick {color} fox {1} over the lazy {0}!"
    string_format_map = "The quick {color} fox {action} over the lazy {animal}!"
    string_identifier = "def";
    string_space = "   "
    string_lines = "The quick brown fox\njumps 0ver \nthe lazy dog!"
    string_strip = "    The quick brown fox jumps 0ver the lazy dog!  "
    string_zfill = "42"
    string_encoded = string.encode()

    print(f'\033[31m capitalize => \033[0m {string.capitalize()}\n') #capitalize the first letter
    print(f'\033[31m strict lowercase => \033[0m{string.casefold()}\n') #strict lowercase
    print(f'\033[31m horizontal padding => \033[0m{string.center(50, "*")}\n') # to padd left and right with a specific character
    print(f'\033[31m count => \033[0m{string.count("0")}\n') #To count the occurence of a substring within a string
    print(f'\033[31m encode => \033[0m{string.encode()}\n') #to convert strings to bytes.
    print(f'\033[31m decode => \033[0m{string_encoded.decode()}\n') #to convert bytes back to strings.
    print(f'\033[31m startswith => \033[0m{string.startswith("quick", 4)}\n') # check whether the string startswith the provided suffix
    print(f'\033[31m endswith => \033[0m{string.endswith("dog!")}\n') #check whether the string endsWith the provided suffix
    print(f'\033[31m custom tabSize => \033[0m{string_with_tab.expandtabs(tabsize=32)}\n') #the \t is converted to space based on the given count
    print(f'\033[31m find => \033[0m{string.find("0v")}\n') #returns the starting index of the word if found, else returns -1
    print(f'\033[31m format => \033[0m{string_format.format("fish", "Hopps", color="blue")}\n') #format string with specified value
    print(f'\033[31m format map => \033[0m{string_format_map.format_map({"color": "cyan", "action": "rolls", "animal" : "donkey"})}\n') ##format string with specified value given as dictionary
    print(f'\033[31m index => \033[0m{string.index("qui")}\n') #similar to find(), but raises valueError when it can't find the substring
    print(f'\033[31m isAlnum => \033[0m{string.isalnum()}\n') #returns true if the string only contains numbers and letters
    print(f'\033[31m isAlpha => \033[0m{string.isalpha()}\n') #returns true if the string consist of only letters
    print(f'\033[31m isDecimel => \033[0m{string.isdecimal()}\n') #returns true if the string is a decimel number(0-9)
    print(f'\033[31m isDigit => \033[0m{string.isdigit()}\n') #returns true if the string consists of digits (eg: decimel or fractions)
    print(f'\033[31m isIdentifier => \033[0m{string_identifier.isidentifier()}\n') #returns true if the string is an identifier
    print(f'\033[31m islower => \033[0m{string.islower()}\n') #returns true if every character is lowercase
    print(f'\033[31m isupper => \033[0m{string.isupper()}\n')  #returns true if every character is uppercase
    print(f'\033[31m isnumber => \033[0m{string.isnumeric()}\n') #returns true if every character is number
    print(f'\033[31m isprintable => \033[0m{string.isprintable()}\n') #checks if there are any characters which cannot be printed and returns false if found
    print(f'\033[31m isspace => \033[0m{string_space.isspace()}\n') #returns true if all characters are spaces.
    print(f'\033[31m istitle => \033[0m{string.istitle()}\n') #returns true if starting letter of words are capitalized
    print(f'\033[31m join =>\033[0m {"-".join(string)}\n') #joins a specific character(s) [delimiter] to all items in an iterable
    print(f'\033[31m lower => \033[0m{string.lower()}\n') #returns string in lowercase
    print(f'\033[31m upper => \033[0m{string.upper()}\n') #returns string in uppercase
    print(f'\033[31m title => \033[0m{string.title()}\n') #capitalize each word
    print(f'\033[31m swapcase => \033[0m{string.swapcase()}\n') #swaps case in the string
    print(f'\033[31m replace => \033[0m{string.replace("fox", "deer")}\n') #replace a substring with another substring
    print(f'\033[31m split => \033[0m{string.split(" ")}\n') #split the string into list of multiple substrings based on a delimiter
    print(f'\033[31m splitlines => \033[0m{string_lines.splitlines(keepends=True)}\n') #it splits string based on newlines (\n), will display \n if keepends is true
    print(f'\033[31m strip => \033[0m{string_strip.strip()}\n') #remove any leading and traling whitespaces
    print(f'\033[31m partition => \033[0m{string.partition("0")}\n') #its splits the string into 3 partitions based on the seperator
    print(f'\033[31m translate & maketrans => \033[0m{string.translate(string.maketrans("fxo", "qzp"))}\n') #modify or remove characters with other characters
    print(f'\033[31m zfill => \033[0m{string_zfill.zfill(10)}\n') #padd the string with 0 until it fills a certain width

def question2():
    cars = ["Ferrari", "Lamborghini", "Porsche", "McLaren", "Bugatti", "Koenigsegg", "Pagani", "Aston Martin", "Maserati", "Lexus"]
    bikes = ["Yamaha", "Kawasaki", "Suzuki", "Ducati", "Harley-Davidson", "BMW Motorrad", "Triumph", "KTM", "Aprilia", "Hero"]


    print(f'\033[31m pop => \033[0m{cars.pop()}\n') #remove item from list end
    cars.append("Rimac"); #append new item to list end
    print(f'\033[31m append => \033[0m{cars}\n')
    cars.insert(0, "Lykan Hypersport") #insert new item at specified index
    print(f'\033[31m insert => \033[0m{cars}\n')
    cars.copy() #copy list
    print(f'\033[31m copy => \033[0m{cars}\n')
    cars.sort() #sort list
    print(f'\033[31m sort => \033[0m{cars}\n')
    cars.reverse() #reverse list
    print(f'\033[31m reverse => \033[0m{cars}\n')
    print(f'\033[31m count => \033[0m{cars.count("Ferrari")}\n') #count the occurrence of an item in the list
    cars.extend(bikes) #append another list
    print(f'\033[31m extend => \033[0m{cars}\n') 
    print(f'\033[31m index => \033[0m{cars.index("Ducati")}\n') #returns the index of occurrence
    cars.remove("Hero") #removes an item
    print(f'\033[31m remove => \033[0m{cars}\n') 
    cars.clear()
    print(f'\033[31m clear => \033[0m{cars}\n')

def question3():
    movies = ["Nayatt", "Manichitrathazhu", "Drishyam", "Premam", "Thondimuthalum Driksakshiyum", "Charlie", "Kumbalangi Nights", "Bangalore Days", "Ustad Hotel", "Pathemari"]

    print(f'\033[31m count => \033[0m{movies.count("Charlie")}')
    print(f'\033[31m index => \033[0m{movies.index("Ustad Hotel")}\n') #returns the index of occurrence

def question4():
    person = {
        "name": "Tony Stark",
        "alias": "Iron Man",
        "age": 45,
        "gender": "Male",
        "occupation": "Genius, Billionaire, Playboy, Philanthropist",
        "city": "Malibu",
        "country": "United States",
        "superpowers": ["Powered Armor Suit", "Genius-level intellect", "Technological expertise"],
        "interests": ["Inventing", "Engineering", "Saving the world"],
        "affiliation": "The Avengers",
        "pet": "Jarvis (AI assistant)"
    }

    print(f'\033[31m copy => \033[0m{person.copy()}\n') #copy dictionary
    print(f'\033[31m fromkeys => \033[0m{person.fromkeys(["name", "superpowers"], "default value")})\n') #creates a new dictionary based on a key list
    print(f'\033[31m get => \033[0m{person.get("occupation")}\n') #get a value based on key
    print(f'\033[31m items => \033[0m{person.items()}\n') #get the items in the dictionary
    print(f'\033[31m keys => \033[0m{person.keys()}\n') #get keys
    print(f'\033[31m values => \033[0m{person.values()}\n') #get values
    print(f'\033[31m pop => \033[0m{person.pop("pet")}\n') #pop a vale based on key
    person.setdefault("status", "Unknown")
    print(f'\033[31m setdefault => \033[0m{person}\n') #add a new key value pair
    person.update({"isAlive": False})
    print(f'\033[31m update => \033[0m{person}\n')
    print(f'\033[31m popitem => \033[0m{person.popitem()}\n')

def question5():
    num1 = 4
    num2 = 2

    def displayText(operator):
        print(f"\033[31m => {operator} operators : on {num1} & {num2}\033[0m")

    def arithmetic():
        print(f"""Addition = {num1+num2}
Subtraction = {num1-num2}
Multiplication = {num1*num2}
Division = {num1/num2}
Modulous = {num1%num2}
exponent = {num1**num2}
floor division = {num1//num2}
        """)

    def assignment(): 
        res = num1 + num2
        print(f"Assignment of 4+2 => {res}\n")
        print("Remainging are arithmetic assignment operators. +=, -=, *=, /*, %=, **=, //=, &=, |=, ^=, >>=, <<=\n")

    def comparison():
        print(f"""less than \033[31m[<]\033[0m = {num1<num2}
greater than \033[31m[>]\033[0m = {num1>num2}
less than or equal to \033[31m[<=]\033[0m = {num1<=num2}
Greater than or equal to \033[31m[>=]\033[0m = {num1>=num2}
not equal to \033[31m[!=]\033[0m = {num1!=num2}
equal to \033[31m[==]\033[0m = {num1==num2}
        """)

    def logical():
        print(f"""
and = {num1>10 and num2<10}
or = {num1>10 or num2>10}
not = {not(num1<=num2)}
        """)

    def identity():
        list1 = [1,2,3,4,5]
        list2 = list1
        list3 = [1,2,3,4,5]
        print(f"""
list1 = {list1}
list2 = list2
list3 = {list3}
        """)
        print(f"list 1 and list 2 \033[31m[is]\033[0m : {list1 is list2} | list1 and list3 \033[31m[is]\033[0m : {list1 is list3}")
        print(f"list 1 and list 2 \033[31m[is not]\033[0m  : {list1 is not list2} | list1 and list3 \033[31m[is not]\033[0m : {list1 is not list3}\n")
    
    def membership():
        sequence = [1, 2, 3, 4, 5]
        print(f"\n3 \033[31m[in]\033[0m {sequence} = {3 in sequence}")
        print(f"33 \033[31m[not in ]\033[0m {sequence} = {33 in sequence}\n")

    def bitwise():
        print(f"""
And = {num1 & num1}
or = {num1 & num1}
not = {~(num1 and num1)}
xor = {num1 ^ num1}
left shift = {num1 << num1}
right shift = {num1 >> num1}
        """)

    displayText("Arithmetic")
    arithmetic()
    displayText("Assignment") 
    assignment()
    displayText("Comparison")
    comparison()
    displayText("Logical") 
    logical()
    displayText("Identity") 
    identity()
    displayText("Membership")
    membership()
    displayText("Bitwise")
    bitwise()

def question6():
    name = input("Enter your name: ")
    print("""\033[31mCountries :\033[0m
1 - India
2 - USA
3 - France
4 - Spain
5 - Japan
    """)
    welcome = ""
    country = ""
    while True:

        choice = int(input("Choose Nationality : "))
        if choice == 0:
            print("Going back")
            break;
        else :
            if choice == 1:
                welcome = "Namaste"
                country = "India"
            elif choice == 2:
                welcome = "Hello"
                country = "USA"
            elif choice == 3:
                welcome = "Bonjour"
                country = "France"
            elif choice == 4:
                welcome = "Hola"
                country = "Spain"
            elif choice == 5:
                welcome = "Konnichiwa"
                country = "Japan"
            else:
                print("Invalid input. try again.")
    
        print(f"{welcome} {name} from {country}\n")
        return


def question7():
    limit = 11
    total = 0
    idx = 0
    while idx <= limit:
        total+=idx
        idx+=1

    print(f'\033[31m SUM \033[0m = {total}')

def question8():
    limit = int(input("Enter the limit : "))
    numbers = []
    for index in range(limit):
        number = int(input(f"Enter number {index+1} : "))
        numbers.append(number)
    print(f"\033[31m numbers before reversing \033[0m  : {numbers}")

    reversed_number = []
    for index in range(limit-1, -1, -1): #range(start, stop(condition), step(loop control))
        reversed_number.append(numbers[index])

    print(f"\033[31m numbers after reversing \033[0m : {reversed_number}")
    
def question9():
    reversed_number = 0
    number = int(input("Enter the number: "))
    print(f'\033[31mbefore reversing \033[0m : {number}')
    while number != 0: 
        #get the last digit and move it up to first position
        last_digit = number % 10
        reversed_number = (reversed_number * 10) + last_digit
        #discard the last digit and repeat the previous step
        number //= 10
    print(f'\033[31mafter reversing \033[0m: {reversed_number}')
    
def question10():
    print("pattern 1:")
    for i in range(6):
        for j in range(i):
            print(j+1, end=" ")
        print("")

def question11():
    print("pattern 2:")
    limit = 5
    for i in range(1,limit+1):
        for j in range(i):
            print("*", end=" ")
            #print(j+1, end=" ")
        print(" ")
    for i in range(limit):
        for j in range(i+1,limit):
            print("*", end=" ")
            #print(j-i, end=" ")
        print(" ")


while True:
    choice = int(input("Enter a question number or enter \033[31m 0 \033[0m to Quit : "))
    if choice == 0:
        print("Quitting...")
        break;
    else :
        getQuestion(choice)
        if choice == 1:
            question1()
        elif choice == 2:
            question2()
        elif choice == 3:
            question3()
        elif choice == 4:
            question4()
        elif choice == 5:
            question5()
        elif choice == 6:
            question6()
        elif choice == 7:
            question7()
        elif choice == 8:
            question8()
        elif choice == 9:
            question9()
        elif choice == 10:
            question10()
        elif choice == 11:
            question11()
        else:
            print("Invalid Input. Please Retry...")
    


