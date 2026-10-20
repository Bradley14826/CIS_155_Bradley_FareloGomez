def calculate_average_grade(grades_dict):
    total = 0
    for grade in grades_dict.values():
        total = total + grade
    average = total / len(grades_dict)
    return average
student_grades = {
    "John": 90,
    "Alice": 85,
    "Bob": 95,
}
result = calculate_average_grade(student_grades)
print("Class Average:", result)