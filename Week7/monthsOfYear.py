def months_of_year(startMonth, endMonth):
    months = ["January", "February", "March", "April",
              "May", "June", "July", "August",
              "September", "October", "November", "December"]

    selectedMonths = months[startMonth:endMonth]
    return selectedMonths

startMonth = int(input("Enter the starting month number: "))
endMonth = int(input("Enter the ending month number: "))

result = months_of_year(startMonth, endMonth)

print("Selected months:", result)