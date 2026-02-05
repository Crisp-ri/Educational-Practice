from typing import Dict, List


def average(grades: List[float]) -> float:
    return sum(grades) / len(grades) if grades else 0.0


if __name__ == "__main__":
    # Example input: mapping student -> list of grades
    grades_input: Dict[str, List[int]] = {
        "Ivan": [5, 4, 3, 5],
        "Maria": [4, 4, 5],
        "Petro": [3, 2, 4],
    }

    # Compute {name: average_grade}
    averages = {name: average(scores) for name, scores in grades_input.items()}

    # Collect unique grades using a set
    unique_grades = set()
    for scores in grades_input.values():
        unique_grades.update(scores)

    # Flatten all grades into a list and compute overall average
    all_grades = [g for scores in grades_input.values() for g in scores]
    overall_avg = average(all_grades)

    print("Per-student averages:")
    for name, avg in averages.items():
        print(f"- {name}: {avg:.2f}")

    print(f"\nUnique grades (count={len(unique_grades)}): {sorted(unique_grades)}")
    print(f"\nOverall average: {overall_avg:.2f}")
