"""
Student Grade Calculator
Author: Xyrad Caballero (BSIT-3R10)
Description: A simple command-line grade calculation tool.
"""

def calculate_weighted_average(scores, weights):
    """Calculate the weighted total grade percentage."""
    total_weighted = sum(score * weight for score, weight in zip(scores, weights))
    total_weight = sum(weights)
    return total_weighted / total_weight if total_weight > 0 else 0.0

def get_letter_grade(percentage):
    """Convert numerical percentage to letter grade."""
    if percentage >= 90.0:
        return "A"
    elif percentage >= 80.0:
        return "B"
    elif percentage >= 70.0:
        return "C"
    elif percentage >= 60.0:
        return "D"
    else:
        return "F"

def get_transmuted_grade(percentage):
    """
    Convert percentage to Philippine collegiate grade scale (1.00 - 5.00).
    1.00 is Excellent, 3.00 is Passing, 5.00 is Failing.
    """
    if percentage >= 97.0:
        return 1.00
    elif percentage >= 94.0:
        return 1.25
    elif percentage >= 91.0:
        return 1.50
    elif percentage >= 88.0:
        return 1.75
    elif percentage >= 85.0:
        return 2.00
    elif percentage >= 82.0:
        return 2.25
    elif percentage >= 79.0:
        return 2.50
    elif percentage >= 76.0:
        return 2.75
    elif percentage >= 75.0:
        return 3.00
    else:
        return 5.00

def main():
    print("=== Student Grade Calculator ===")
    print("Welcome! Core grade logic loaded.\n")

if __name__ == "__main__":
    main()
