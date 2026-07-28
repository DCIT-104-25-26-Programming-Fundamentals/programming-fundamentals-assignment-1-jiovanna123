# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 2
# Topic: Conditional Logic (if / elif / else) and Functions
# =============================================================================

def get_grade(score):
    """
    Validates the score and determines the letter grade.
    Returns the grade letter as a string, or None if invalid.
    """
    # Requirement: Validate that score is within 0-100 range
    if score < 0 or score > 100:
        return None

    # Determine grade using if / elif / else
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"


def main():
    # Prompt user for score input
    score = float(input("Enter student score (0-100): "))

    # Get letter grade
    grade = get_grade(score)

    # Print result or error message depending on validity
    if grade is None:
        print("Error: Score must be between 0 and 100.")
    else:
        print(f"Grade: {grade}")


# Main execution block
if __name__ == "__main__":
    main()
