
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b


def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b


def divide(a, b):
    """
    Returns the quotient of two numbers rounded to 2 decimal places.
    Raises ZeroDivisionError if b is 0.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return round(a / b, 2)


def modulus(a, b):
    """
    Returns the remainder of division of two numbers.
    Raises ZeroDivisionError if b is 0.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a % b


def power(a, b):
    """Returns a raised to the power of b."""
    return a ** b


def display_menu():
    """Prints the calculator menu options."""
    print("\n============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def format_number(val):
    """Helper to convert float whole numbers (e.g. 10.0) into clean ints (10)."""
    return int(val) if val.is_integer() else val


def main():
    while True:
        display_menu()
        choice = input("Select an operation (1-7): ").strip()

        if choice == "7":
            print("Goodbye!")
            break

        if choice in ("1", "2", "3", "4", "5", "6"):
            try:
                num1 = float(input("Enter first number : "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Error: Invalid input. Please enter valid numbers.")
                continue

            
            f_num1 = format_number(num1)
            f_num2 = format_number(num2)

            try:
                if choice == "1":
                    res = add(num1, num2)
                    print(f"Result: {f_num1} + {f_num2} = {format_number(res)}")
                elif choice == "2":
                    res = subtract(num1, num2)
                    print(f"Result: {f_num1} - {f_num2} = {format_number(res)}")
                elif choice == "3":
                    res = multiply(num1, num2)
                    print(f"Result: {f_num1} * {f_num2} = {format_number(res)}")
                elif choice == "4":
                    res = divide(num1, num2)
                    print(f"Result: {f_num1} / {f_num2} = {res}")
                elif choice == "5":
                    res = modulus(num1, num2)
                    print(f"Result: {f_num1} % {f_num2} = {format_number(res)}")
                elif choice == "6":
                    res = power(num1, num2)
                    print(f"Result: {f_num1} ** {f_num2} = {format_number(res)}")
            except ZeroDivisionError as e:
                print(f"Error: {e}")
        else:
            print("Invalid choice! Please select an operation from 1 to 7.")


 
if __name__ == "__main__":
    main()
