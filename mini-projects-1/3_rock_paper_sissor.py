#enter user input 
#enter computer input

import _helper as hp
from _helper import Colors
import random
from enum import Enum

class Player(Enum):
    USER = 0
    COMPUTER = 1
    NONE = 2

user_wins, computer_wins = 0,0

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return Player.NONE
    elif (user_choice == 'rock' and computer_choice == 'sissor') or \
        (user_choice == 'paper' and computer_choice == 'rock') or \
        (user_choice == 'sissor' and computer_choice == 'paper'):
            return Player.USER
    else:
        return Player.COMPUTER

def get_result(winner):
        global user_wins, computer_wins
        if winner == Player.USER:
            user_wins +=1
            print(hp.ct(Colors.GREEN,"You've Won!"))
        elif winner == Player.COMPUTER:
            computer_wins +=1
            print(hp.ct(Colors.YELLOW,"Computer Won!"))
        else:
            print(hp.ct(Colors.YELLOW,"Its a tie!"))


def main():
    options = ["rock", "paper", "sissor"]
    while True:
        winner = Player.NONE
        user_choice = input(f"Enter rock/paper/sissor or {hp.ct(Colors.RED, "x")} to quit: ").strip().lower()
        
        random_index = random.randint(0,2)
        computer_choice = options[random_index]

        if user_choice == 'x':
            print(f"Quitting...\n\nYou've won {user_wins} times.\nComputer won {computer_wins} times.")
            exit()
        elif user_choice not in options:
            print(hp.ct(Colors.RED, "Invalid input! Please enter rock, paper, or sissor."))
            continue
        
        print(f"Computper choose - {computer_choice}")
        winner = get_winner(user_choice, computer_choice)

        get_result(winner)
        

if __name__ == "__main__":
    main()
