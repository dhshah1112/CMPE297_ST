from typing import List, Union
from functools import lru_cache

def is_even(number: int) -> bool:
    """
    Check if a number is even.
    
    :param number: int, the number to check
    :return: bool, True if the number is even, False otherwise
    """
    return number % 2 == 0

def capitalize_words(sentence: str) -> str:
    """
    Capitalize the first letter of each word in a sentence.
    
    :param sentence: str, the input sentence
    :return: str, the sentence with each word capitalized
    """
    return sentence.title()

@lru_cache(maxsize=None)
def _fib(n: int) -> int:
    if n < 2:
        return n
    return _fib(n-1) + _fib(n-2)

def fibonacci(n: int) -> List[int]:
    """
    Generate the Fibonacci sequence up to the nth number.
    
    :param n: int, the number of Fibonacci numbers to generate
    :return: List[int], the Fibonacci sequence
    :raises ValueError: if n is negative
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    return [_fib(i) for i in range(n)]

def safe_divide(a: float, b: float) -> Union[float, str]:
    """
    Safely divide two numbers, handling division by zero.
    
    :param a: float, numerator
    :param b: float, denominator
    :return: float if division is successful, str with error message otherwise
    """
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception as e:
        return f"Error: {str(e)}"
    else:
        return result

def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.
    
    :param n: int, the number to calculate the factorial of
    :return: int, the factorial of n
    :raises ValueError: if n is negative
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)