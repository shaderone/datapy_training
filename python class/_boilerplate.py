questions = """

1. Demonstrate Simple inheritance for Arithmetic class

2. Demonstrate Multilevel inheritance for Employee class

3. Demonstrate Multiple inheritance for Student class

4. Demonstrate Heirarchial inheritance for Polygon class

"""

questions_list = questions.strip().split("\n")

def getQuestion(index):
    index-=1
    print("\n",questions_list[index], "\n")
    


def main():
    while True:
        try:
            choice = int(input("Enter a question number or enter \033[31m 0 \033[0m to Quit : "))
            if choice == 0:
                print("Quitting...")
                break;
            elif 0 < choice <= 4 :
                getQuestion(choice)
                if choice == 1:
                    
                    print("\n")
                elif choice == 2:
                    
                    print("\n")
                elif choice == 3:
                    
                    print("\n")
                elif choice == 4:
                    print("\n")
            else :
                print("Invalid Input. Please Retry...")

        except ValueError:
            print("Invalid Input. Please Retry...")
            
if __name__ == "__main__":
    main()


"""
# ? Helper class --------------------------------------------------------

class ColoredStringMeta(type):
    RESET = '\033[0m'
    COLORS = {
        'red': '\033[31m',
        'black': '\033[30m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
    }
    # ? __getattr__() is used to dynamically generate colors, based on a given attribute or "accessed attribute"
    # ? if the attribute is not found, __getattr__() get called.
    def __getattr__(cls, attr):
        print("in getattr")
        # ? cls = ColoredString (the class which metaclass is responsible for creating), attr = attribute being accessed
        if attr in cls.COLORS:
            return lambda self: f"{cls.COLORS[attr]}{self}{cls.RESET}"
        else:
            return lambda self: self # ! return string if requested color is not found
    
    # ! self will have the value passed as argument. It is accessible on this metaclass because __getattr__() gets called because the attribute the instance is trying to access has not been found. And __getattr__() is defined in the metaclass. so the metaclass will have access to the value passed to the instance of the `ColoredString`

# ? Here ColoredString extends or inherits 'str' class thereby getting it properties.
class ColoredString(str, metaclass=ColoredStringMeta):
#
#    

# ? Helper class --------------------------------------------------------
"""