import os
from enum import Enum

class Colors(Enum):
    RED = '\033[31m'
    BLACK = '\033[30m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    _RESET = '\033[0m'

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def ct(color, data):
    """Gives color to a given string"""
    return f'{color.value}{data}{Colors._RESET.value}'

