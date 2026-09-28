import math

def calculate_angle(x, y):
    theta = math.atan2(y, x) * (180 / math.pi)
    print("The angle theta is:", theta, "degrees")

x = float(input("Enter the value for x: "))
y = float(input("Enter the value for y: "))

calculate_angle(x, y)