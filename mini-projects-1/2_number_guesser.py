#generate a random number
#track the times it takes to guess correctly

import _helper as hp
from _helper import Colors
import random

def main():
    number = random.randint(0,10)
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
            elif(guess != number):
                print(f"Enter your Guess [{tries}] : {guess} {hp.ct(Colors.RED, "try again!")}")
                tries+=1
        except ValueError:
            print(hp.ct(Colors.RED, "Enter numbers only!"))

    if(tries > limit):
        print(hp.ct(Colors.RED, "Game Over!\n"))     

if __name__ == "__main__":
    main()

