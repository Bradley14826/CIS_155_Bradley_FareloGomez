def isPalindrome(word):
    reversedWord = word[::-1]

    if word == reversedWord:
        return True
    else:
        return False

word = input("Enter a string of at least 5 characters: ")

result = isPalindrome(word)

if result == True:
    print(f"The string {word} is a palindrome.")
else:
    print(f"The string {word} is NOT a palindrome.")