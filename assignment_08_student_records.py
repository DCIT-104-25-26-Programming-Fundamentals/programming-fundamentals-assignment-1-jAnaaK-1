# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# Student Record System


# A console-based program to manage and track student information

students = []


def display_menu():
    """Display the main menu options."""
    print("\n================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")
    print()


def add_student():
    """Add a new student record with name, ID, and scores."""
    try:
        name = input("Student name: ").strip()
        if not name:
            print("Error: Student name cannot be empty.")
            return
        
        student_id = int(input("Student ID: ").strip())
        
        # Check if ID already exists
        for student in students:
            if student["id"] == student_id:
                print(f"Error: A student with ID {student_id} already exists.")
                return
        
        num_scores = int(input("How many scores? "))
        if num_scores < 1:
            print("Error: Number of scores must be at least 1.")
            return
        
        scores = []
        for i in range(1, num_scores + 1):
            try:
                score = float(input(f"Enter score {i}: "))
                if 0 <= score <= 100:  # Assuming scores are between 0-100
                    scores.append(score)
                else:
                    print("Error: Score must be between 0 and 100.")
                    return
            except ValueError:
                print("Error: Please enter a valid number for the score.")
                return
        
        student = {
            "name": name,
            "id": student_id,
            "scores": scores
        }
        students.append(student)
        print(f'Student "{name}" added successfully.')
    
    except ValueError:
        print("Error: Please enter valid input (ID must be a number).")


def calculate_average(scores):
    """Calculate and return the average of a list of scores."""
    if not scores:
        return 0
    return sum(scores) / len(scores)


def display_all_students():
    """Display a formatted table of all students with their information."""
    if not students:
        print("No students have been added yet.")
        return
    
    print("-" * 65)
    print(f"{'Name':<20} {'ID':<12} {'Scores':<20} {'Average':<10}")
    print("-" * 65)
    
    for student in students:
        name = student["name"]
        student_id = student["id"]
        scores = student["scores"]
        average = calculate_average(scores)
        
        # Format scores as comma-separated values
        scores_str = ", ".join(str(int(s) if s == int(s) else s) for s in scores)
        
        print(f"{name:<20} {student_id:<12} {scores_str:<20} {average:.2f}")
    
    print("-" * 65)


def calculate_student_average():
    """Find a student by ID and display their average score."""
    if not students:
        print("No students in the system.")
        return
    
    try:
        student_id = int(input("Enter student ID: "))
        
        for student in students:
            if student["id"] == student_id:
                name = student["name"]
                average = calculate_average(student["scores"])
                print(f"{name}'s average score: {average:.2f}")
                return
        
        print(f"Error: Student with ID {student_id} not found.")
    
    except ValueError:
        print("Error: Please enter a valid student ID (number).")


def quit_program():
    """Exit the program with a farewell message."""
    print("Goodbye!")
    return False


def main():
    """Main program loop to run the student record system."""
    running = True
    
    while running:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            add_student()
        elif choice == "2":
            display_all_students()
        elif choice == "3":
            calculate_student_average()
        elif choice == "4":
            running = quit_program()
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()

# =============================================================================

