import math

def calculate_hypotenuse(x, y):
    c = math.sqrt((x ** 2) + (y ** 2))
    print("The hypotenuse is:", c)

x = float(input("Enter the value for x: "))
y = float(input("Enter the value for y: "))

calculate_hypotenuse(x, y)