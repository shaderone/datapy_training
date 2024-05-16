#ask question
#add point for right answer
#show result
import _helper as hp
from _helper import Colors
from enum import Enum

import sys

class GameStatus(Enum):
    PLAY = "p"
    CLEAR = 'c'
    QUIT = ""

prompt = (
    f"Press {hp.ct(Colors.RED, 'P')} to Play {hp.ct(Colors.BLUE, '|')} "
    f"Press {hp.ct(Colors.RED, 'C')} to Clear {hp.ct(Colors.BLUE, '|')} "
    f"Press {hp.ct(Colors.RED, '↵')} to Quit {hp.ct(Colors.BLUE, '')} : "
)

questions_and_answers = {
    "What is the capital of France? ": "Paris",
    "What is 5 + 7? ": "12",
    "Who wrote 'To Kill a Mockingbird'? ": "Harper Lee",
    "What is the square root of 64? ": "8",
    "What is the chemical symbol for water? ": "H2O",
    "In which year did the Titanic sink? ": "1912",
    "Who painted the Mona Lisa? ": "Leonardo da Vinci",
    "What is the largest planet in our solar system? ": "Jupiter",
    "What is the freezing point of water in degrees Celsius? ": "0",
    "What is the tallest mountain in the world? ": "Mount Everest"
}

def start_quiz():
    score = 0
    for question, correct_answer in questions_and_answers.items():
        answer = input(question).strip().lower()
        #print(CURSOR_UP_ONE + CURSOR_UP_ONE) # will work because the duplicate print() exceeds the input() promt length.
        hp.clear_line()
        if answer == correct_answer.lower():
            print(f"{question}{answer} here - {hp.ct(Colors.GREEN,"✔")}")
            score+=1
        else:
            print(f"{question}{answer} hehe - {hp.ct(Colors.RED,"X")} The correct answer is {hp.ct(Colors.BLUE,correct_answer)}.")
    
    return score


def main():
    while True:
        try:
            print(f"{"Welcome to simple quiz".center(50,"-")}\n")

            game_status = input(prompt).strip().lower()
            match(game_status):
                case GameStatus.PLAY.value:
                    print(f"{hp.ct(Colors.YELLOW,"Quiz Started...")}\n")
                    score = start_quiz()
                    print(f'You scored {hp.ct(Colors.GREEN,score)} out of {hp.ct(Colors.BLUE,len(questions_and_answers.items()))}\n')
                case GameStatus.CLEAR.value:
                    hp.clear_console()
                case GameStatus.QUIT.value:
                    hp.clear_console()
                    print("Goodbye.")
                    exit()
                case _:
                    print(hp.ct(Colors.RED, "Invalid input! Please press 'P' to Play or '↵' to Quit."))
                    break;
        
        except ValueError:
            print(hp.ct(Colors.RED, "Invalid input! Please press 'P' to Play or '↵' to Quit."))



if __name__ == "__main__":
    main()