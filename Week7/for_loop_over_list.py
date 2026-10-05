def getMyList():
    myList = [10, 20, 30, 40, 50, 60]
    counter = 0
    for number in myList:
        print(number)
        counter= counter + 1
    return counter
iterations = getMyList()
print("The function call looped", iterations, "times.")