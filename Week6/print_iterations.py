def print_iterations(val):
    loopCounter = 0

    for counter in range(val):
        loopCounter = loopCounter + 1

    return loopCounter

val = int(input("Enter the number of iterations: "))

loopCounter = print_iterations(val)

print("The function call looped", loopCounter, "times.")