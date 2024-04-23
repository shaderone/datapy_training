#prime number
import math

class IncorrectInputException(Exception):
    """
    Custom Exception to handle cases where the input provided is of an incorrect type.
    """
    def __init__(self, number, input_type):
        self.number = number
        self.input_type = input_type

    def __str__(self):
        return f"The number you entered [{self.number}] is of incorrect type [{self.input_type}]. Please enter a valid Integer"

def check_input_type(number):
    if(type(number) != int):
        raise IncorrectInputException(number, type(number))

def check_prime(number):

    check_input_type(number)

    if(number == 0 or number == 1):
        return f"{number} is neither prime nor composite"
    elif(number < 0):
        return "Negative numbers cannot be prime numbers"
    else:
        #we check up to the square root of the number, because if the divisors are greater than the number itself then their product( will also be greater than the number, so there is no point in furthur checking.
        for i in range(2, math.isqrt(number)+1):
            if(number % i == 0):
                return f"{number} is not prime"
        
        return f"{number} is prime"

#factoarial
def get_factorial(number):
    fact = 1
    
    check_input_type(number)
    
    if number in (0,1):
        return f"Factorial of {number} is 1"
    elif(number < 0):
        return f"Factorial of Negative numbers is NOT DEFINED"
    else:
        for i in range(1, number+1):
            fact *= i
        
        return fact

#fibonacci series
def get_fibonacci(number):
    previous_number, next_number = 0, 1
    fibonacci_series = ""
    check_input_type(number)

    if(number == 0):
        return str(number)
    elif(number < 0):
        return f"Fibonacci of Negative numbers is NOT AVAILABLE"
    else:
        for _ in range(number):
            fibonacci_series += str(previous_number) + " "
            previous_number, next_number = next_number, previous_number + next_number
        
        return fibonacci_series

#armstrong number
def check_armstrong(number):
    check_input_type(number)

    if number in (0,1):
        return f"{number} is Armstrong number"
    elif(number < 0):
        return "Negative numbers cannot be Armstrong numbers"
    else:
        digit_cube_sum = 0
        for digit in str(number):
            digit_cube_sum += (int(digit) ** len(str(number)))

        return f"{number} is Armstrong" if digit_cube_sum == number else f"{number} is not Armstrong"

#sun of 'n' numbers
def get_sum(number):
    total = 0
    for i in range(number+1):
        total += i
    
    return total