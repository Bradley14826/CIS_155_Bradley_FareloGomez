def validateCreditCard(ccNum):
    total = 0
    reverseNum = ccNum[::-1]
    for i in range(len(reverseNum)):
        digit = int(reverseNum[i])
        if i % 2 == 1:
            digit = digit * 2
            if digit > 9:
                digit = digit - 9
        total = total + digit 
    return total % 10 == 0
while True:
    ccNum = input("Enter a credit card number: ")
    if ccNum.isdigit() and validateCreditCard(ccNum):
        print(f"The credit card number {ccNum} is valid!")
        break
    else:
        print(f"Invalid credit card entered. Please try again.")