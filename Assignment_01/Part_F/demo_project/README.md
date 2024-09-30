# Demo Project

This is a simple demo project showcasing various Python programming concepts and best practices.

## Project Structure

```
demo_project/
├── src/
│   ├── main.py
│   └── utils.py
├── tests/
│   └── test_utils.py
└── README.md
```

## Features

- Greeting function
- Basic arithmetic operations
- Even number checker
- Word capitalization
- Fibonacci sequence generator
- Safe division with error handling

## Usage

To run the project, use the following command:

```
python src/main.py <action> [arguments]
```

Available actions:
- `greet`: Greet a person
- `sum`: Calculate the sum of two numbers
- `even`: Check if a number is even
- `capitalize`: Capitalize words in a sentence
- `fib`: Generate Fibonacci sequence
- `divide`: Safely divide two numbers

Examples:
```
python src/main.py greet World
python src/main.py sum 5 3
python src/main.py even 4
python src/main.py capitalize hello world
python src/main.py fib 10
python src/main.py divide 10 2
```

## Running Tests

To run the unit tests, use the following command:

```
python -m unittest discover tests
```

## Contributing

Feel free to submit issues and pull requests for any improvements or bug fixes.