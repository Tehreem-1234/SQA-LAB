"""Simple student grade manager."""


def average(marks):
    """Return the average of a list of marks."""
    if not marks:
        raise ValueError("marks list cannot be empty")
    return sum(marks) / len(marks)


def letter_grade(score):
    """Convert a numeric score (0-100) to a letter grade."""
    if score < 0 or score > 100:
        raise ValueError("score must be between 0 and 100")
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def highest(marks):
    """Return the highest mark."""
    if not marks:
        raise ValueError("marks list cannot be empty")
    return max(marks)


def lowest(marks):
    """Return the lowest mark."""
    if not marks:
        raise ValueError("marks list cannot be empty")
    return min(marks)


def is_passing(score, pass_mark=50):
    """Return True if score is at or above the pass mark."""
    return score >= pass_mark


def class_report(students):
    """Build a report dict {name: (average, grade)} from {name: [marks]}."""
    report = {}
    for name, marks in students.items():
        avg = average(marks)
        report[name] = (round(avg, 2), letter_grade(avg))
    return report
