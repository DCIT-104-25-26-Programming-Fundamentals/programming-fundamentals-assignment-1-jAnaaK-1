# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================

# Multiplication Table

# Asking the user to enter a number
number = int(input("Enter a number: "))

# Printing the multiplication table from 1 to 12
for i in range(1, 13):
    print(f"{number} x {i} = {number * i}")





# Multiplication Tables from 1 to N

# Asking the user to enter a number
N = int(input("Enter a number: "))

# Printing the multiplication table for every number from 1 to N
if N > 0:
    for i in range(1, N + 1):
        print(f"\nMultiplication Table of {i}")
        
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")


    # Separator line
    print("--------------------")

if N <= 0:
    print("Error: Please enter a positive integer.")
    



# =============================================================================

