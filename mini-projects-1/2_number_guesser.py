#generate a random number
#track the times it takes to guess correctly

#make user choose the limit
#narrow down guess range when it's wrong.

import _helper as hp
from _helper import Colors
import random

def main():
    max_range = int(input("Enter the range of number to be guessed : "))
    number = random.randint(0,max_range+1)
    tries = 1
    limit = 5

    print(number)
    while(tries <= limit):
        try:
            guess = int(input(f"Enter your Guess [{tries}] : "))
            hp.clear_line()
            if(guess == number):
                print(f"Enter your Guess [{tries}] : {guess} {hp.ct(Colors.GREEN, "is correct.")}")
                print(hp.ct(Colors.YELLOW, f"you took {tries} tries\n"))
                break;
            elif(guess >= number):
                print(f"Enter your Guess [{tries}] : {guess} {hp.ct(Colors.RED, "try lower!")}")
                tries+=1
            elif(guess <= number):
                print(f"Enter your Guess [{tries}] : {guess} {hp.ct(Colors.RED, "try higher!")}")
                tries+=1
        except ValueError:
            print(hp.ct(Colors.RED, "Enter numbers only!"))

    if(tries > limit):
        print(hp.ct(Colors.RED, "Game Over!\n"))     

if __name__ == "__main__":
    main()

