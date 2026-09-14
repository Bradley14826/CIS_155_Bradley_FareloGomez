number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

result = number1 - number2

print("The result is:", result)

if result < 0:
    print("############################")
    print("Invalid! The value is less than zero")
    print("############################")
else:
    print("The values entered were valid integers.")