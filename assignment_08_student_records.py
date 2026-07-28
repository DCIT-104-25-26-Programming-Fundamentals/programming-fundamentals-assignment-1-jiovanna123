
def display_menu():
    """Prints the main menu options."""
    print("\n================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def add_student(students):
    """
    Prompts user for student's name, ID, and list of assessment scores,
    then adds the student record dictionary to the list.
    """
    name = input("Student name: ").strip()
    student_id = input("Student ID: ").strip()

    num_scores = int(input("How many scores? "))
    scores = []
    for i in range(1, num_scores + 1):
        score = float(input(f"Enter score {i}: "))
        
        if score.is_integer():
            score = int(score)
        scores.append(score)

    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }

    students.append(student)
    print(f'Student "{name}" added successfully.')


def display_all_students(students):
    """
    Displays a formatted table showing every student's Name, ID, Scores,
    and rounded average score.
    """
    if not students:
        print("No student records available.")
        return

    print("-" * 50)
    print(f"{'Name':<15} {'ID':<11} {'Scores':<14} {'Average'}")
    print("-" * 50)

    for student in students:
        name = student["name"]
        sid = str(student["id"])
        scores_str = ", ".join(str(s) for s in student["scores"])

        if student["scores"]:
            avg = sum(student["scores"]) / len(student["scores"])
            avg_str = f"{avg:.2f}"
        else:
            avg_str = "N/A"

        print(f"{name:<15} {sid:<11} {scores_str:<14} {avg_str}")

    print("-" * 50)


def calculate_student_average(students):
    """
    Prompts for a student ID, finds the student, and displays
    their calculated average score rounded to 2 decimal places.
    """
    target_id = input("Enter student ID: ").strip()

    for student in students:
        if str(student["id"]) == target_id:
            if student["scores"]:
                avg = sum(student["scores"]) / len(student["scores"])
                print(f"{student['name']}'s average score: {avg:.2f}")
            else:
                print(f"{student['name']} has no scores recorded.")
            return

    print(f"Error: Student ID '{target_id}' not found.")


def main():
    students = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_all_students(students)
        elif choice == "3":
            calculate_student_average(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()



