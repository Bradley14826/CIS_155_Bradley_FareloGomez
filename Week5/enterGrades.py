count = 0
total_grades = int(input("How many grades do you want to enter? "))
while counter < total_grades:
    grade = int(input("Enter a grade: "))
    print("Grade entered:", grade)
    counter = counter + 1
    print("The user has entered", total_grades, "grades and is now done")
