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

def get_valid_score(prompt, min_val=0.0, max_val=100.0):
    """Safely prompt user for a float score within range."""
    while True:
        try:
            val = float(input(prompt).strip())
            if min_val <= val <= max_val:
                return val
            print(f"  [Error] Score must be between {min_val} and {max_val}.")
        except ValueError:
            print("  [Error] Please enter a valid numerical score.")

def run_grade_calculator():
    """Runs interactive student grade entry and displays score summary."""
    print("==================================================")
    print("             STUDENT GRADE CALCULATOR             ")
    print("==================================================")
    
    student_name = input("Enter Student Name: ").strip() or "Student"
    subject_code = input("Enter Subject Code/Name: ").strip() or "IT Subject"

    components = [
        {"name": "Quizzes", "weight": 20},
        {"name": "Assignments & Activities", "weight": 20},
        {"name": "Midterm Examination", "weight": 25},
        {"name": "Final Examination", "weight": 35},
    ]

    print(f"\nEntering scores (0 - 100) for {subject_code}:")
    scores = []
    weights = []

    for item in components:
        score = get_valid_score(f"  > {item['name']} ({item['weight']}%): ")
        item["score"] = score
        scores.append(score)
        weights.append(item["weight"])

    final_percentage = calculate_weighted_average(scores, weights)
    transmuted = get_transmuted_grade(final_percentage)
    letter = get_letter_grade(final_percentage)

    print("\n--------------------------------------------------")
    print(f"GRADE REPORT: {student_name} | {subject_code}")
    print("--------------------------------------------------")
    for item in components:
        weighted_contribution = (item["score"] * item["weight"]) / 100.0
        print(f" - {item['name']:<28}: {item['score']:>6.2f} / 100 (Contrib: {weighted_contribution:>5.2f}%)")
    
    print("--------------------------------------------------")
    print(f"Final Percentage : {final_percentage:.2f}%")
    print(f"Collegiate Grade : {transmuted:.2f}")
    print(f"Letter Grade     : {letter}")
    print("==================================================\n")

def main():
    run_grade_calculator()

if __name__ == "__main__":
    main()
