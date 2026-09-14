number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

result = number1 // number2

print("The result is:", result)

if result > 5 and result < 7:
    print("The number is between 5 and 7")
else:
    print("The number is out of range!")