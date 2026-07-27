# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 1
# Topic: Conditional Logic, Loops, and Functions
# =============================================================================
#
# TASK: Prime Number Checker
#
# Write a Python program that checks whether a given number is prime.
#
# A prime number is a whole number greater than 1 that has no divisors
# other than 1 and itself (e.g., 2, 3, 5, 7, 11, 13 ...).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLES
# -----------------------------------------------------------------------------
#
#   Enter a number: 7
#   7 is a prime number.
#
#   Enter a number: 10
#   10 is NOT a prime number.
#
#   Enter a number: 1
#   1 is NOT a prime number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement the logic inside a function (see scaffold below).
# - Numbers less than 2 are NOT prime — handle this inside the function.
# - The main block must call the function and print the result.
#

# =============================================================================
#1. "Enter a number" for the input.
#2. check whether the numeber is prime using the modulus operator
#logic behind modulus operator is...if the number is prime the the result should be 0 mod the number
#Create a function which would disqualify numbers less than 2 automatically.

testnumber = int(input("Enter a number: "))

def PrimeCheck(testnumber):
    if testnumber < 2:
        return False
    elif testnumber == 2:
        return True
    elif testnumber % 2 == 0:
        return False
    else:
        for i in range(3, int(testnumber**0.5) + 1, 2):
            if testnumber % i == 0:
                return False
        return True

if PrimeCheck(testnumber):
    print(f"{testnumber} is a prime number.")
else:
    print(f"{testnumber} is NOT a prime number.")



# =============================================================================