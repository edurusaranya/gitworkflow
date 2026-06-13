"""A simple calculator module demonstrating a basic Python project."""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the quotient of a and b. Raises ValueError on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    print("Simple Calculator")
    print("Operations: add, subtract, multiply, divide")

    op = input("Enter operation: ").strip().lower()
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    if op not in operations:
        print(f"Unknown operation: {op}")
        return

    try:
        result = operations[op](a, b)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
