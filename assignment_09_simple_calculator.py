# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# Simple Calculator Program
# A console-based calculator for basic arithmetic operations

def display_menu():
    """Display the calculator menu."""
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
    print()


def get_numbers():
    """Prompt the user to enter two numbers and return them."""
    try:
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Error: Please enter valid numbers.")
        return None, None


def add(num1, num2):
    """Perform addition."""
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")


def subtract(num1, num2):
    """Perform subtraction."""
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")


def multiply(num1, num2):
    """Perform multiplication."""
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")


def divide(num1, num2):
    """Perform division with zero-division error handling."""
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = round(num1 / num2, 2)
        print(f"Result: {num1} / {num2} = {result}")


def modulus(num1, num2):
    """Perform modulus (remainder) operation."""
    if num2 == 0:
        print("Error: Cannot perform modulus with zero.")
    else:
        result = num1 % num2
        print(f"Result: {num1} % {num2} = {result}")


def exponentiation(num1, num2):
    """Perform exponentiation."""
    result = num1 ** num2
    print(f"Result: {num1} ** {num2} = {result}")


def quit_calculator():
    """Exit the calculator."""
    print("Goodbye!")
    return False


def main():
    """Main program loop for the calculator."""
    running = True
    
    while running:
        display_menu()
        choice = input("Select an operation (1-7): ").strip()
        
        if choice == "1":
            num1, num2 = get_numbers()
            if num1 is not None and num2 is not None:
                add(num1, num2)
        
        elif choice == "2":
            num1, num2 = get_numbers()
            if num1 is not None and num2 is not None:
                subtract(num1, num2)
        
        elif choice == "3":
            num1, num2 = get_numbers()
            if num1 is not None and num2 is not None:
                multiply(num1, num2)
        
        elif choice == "4":
            num1, num2 = get_numbers()
            if num1 is not None and num2 is not None:
                divide(num1, num2)
        
        elif choice == "5":
            num1, num2 = get_numbers()
            if num1 is not None and num2 is not None:
                modulus(num1, num2)
        
        elif choice == "6":
            num1, num2 = get_numbers()
            if num1 is not None and num2 is not None:
                exponentiation(num1, num2)
        
        elif choice == "7":
            running = quit_calculator()
        
        else:
            print("Error: Invalid choice. Please select a number between 1 and 7.")


if __name__ == "__main__":
    main()

# =============================================================================

