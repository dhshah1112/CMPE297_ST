import argparse
from typing import Any
from utils import is_even, capitalize_words, fibonacci, safe_divide

def greet(name: str) -> str:
    """
    Returns a greeting message for the given name.
    
    :param name: str, name of the person to greet
    :return: str, greeting message
    """
    return f"Hello, {name}!"

def calculate_sum(a: float, b: float) -> float:
    """
    Calculates the sum of two numbers.
    
    :param a: float, first number
    :param b: float, second number
    :return: float, sum of a and b
    """
    return a + b

def main() -> None:
    """
    Main function to handle CLI arguments and execute corresponding functions.
    """
    parser = argparse.ArgumentParser(description="Demo project CLI")
    parser.add_argument("action", choices=["greet", "sum", "even", "capitalize", "fib", "divide"],
                        help="Action to perform")
    parser.add_argument("args", nargs="*", help="Arguments for the action")

    args = parser.parse_args()

    if args.action == "greet":
        if len(args.args) != 1:
            print("Usage: python main.py greet <name>")
        else:
            print(greet(args.args[0]))
    elif args.action == "sum":
        if len(args.args) != 2:
            print("Usage: python main.py sum <number1> <number2>")
        else:
            try:
                result = calculate_sum(float(args.args[0]), float(args.args[1]))
                print(f"Sum: {result}")
            except ValueError:
                print("Error: Please provide valid numbers")
    elif args.action == "even":
        if len(args.args) != 1:
            print("Usage: python main.py even <number>")
        else:
            try:
                result = is_even(int(args.args[0]))
                print(f"Is even: {result}")
            except ValueError:
                print("Error: Please provide a valid integer")
    elif args.action == "capitalize":
        print(capitalize_words(" ".join(args.args)))
    elif args.action == "fib":
        if len(args.args) != 1:
            print("Usage: python main.py fib <number>")
        else:
            try:
                result = fibonacci(int(args.args[0]))
                print(f"Fibonacci sequence: {result}")
            except ValueError as e:
                print(f"Error: {str(e)}")
    elif args.action == "divide":
        if len(args.args) != 2:
            print("Usage: python main.py divide <number1> <number2>")
        else:
            try:
                result = safe_divide(float(args.args[0]), float(args.args[1]))
                print(f"Result: {result}")
            except ValueError:
                print("Error: Please provide valid numbers")

if __name__ == "__main__":
    main()