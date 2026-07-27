# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================



number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))
number3 = int(input("Enter number 3: "))   
number4 = int(input("Enter number 4: "))
number5 = int(input("Enter number 5: "))

def Sumofnumbers(number1,number2,number3,number4,number5):
    total = number1 + number2 + number3 + number4 + number5
    return total

def Averageofnumbers(total, count):
    average = total / count
    return average

def Maximumofnumbers(number1,number2,number3,number4,number5):
        maximum = number1
        if number2 > maximum:
            maximum = number2
        if number3 > maximum:
            maximum = number3
        if number4 > maximum:
            maximum = number4
        if number5 > maximum:
            maximum = number5
        return maximum

def Minimumofnumbers(number1,number2,number3,number4,number5):
        minimum = number1
        if number2 < minimum:
            minimum = number2
        if number3 < minimum:
            minimum = number3
        if number4 < minimum:
            minimum = number4
        if number5 < minimum:
            minimum = number5
        return minimum

print(f"Sum: {Sumofnumbers(number1, number2, number3, number4, number5)}")
print(f"Average: {Averageofnumbers(Sumofnumbers(number1, number2, number3, number4, number5), 5)}")
print(f"Maximum: {Maximumofnumbers(number1, number2, number3, number4, number5)}")
print(f"Minimum: {Minimumofnumbers(number1, number2, number3, number4, number5)}")

# =============================================================================

