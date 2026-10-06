def append_to_list(item, target_list):
    target_list.append(item)
my_list = []
item = input("Enter a vaule:")
append_to_list(item, my_list)
while True:
    answer = input("Would you like to enter another vaule to append to this list? (y or n) ")
    if answer == "y":
        item = input("Enter another value: ")
        append_to_list(item, my_list)
    elif answer == "n":
        break
    else:
        print("Sorry, you have entered an invalide vaule, please try again")
print(my_list)


