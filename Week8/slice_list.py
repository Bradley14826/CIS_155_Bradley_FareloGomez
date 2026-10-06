def slice_list(month_list):
    sliced_months = month_list[4:7]
    return sliced_months 
months = ["January", "February", "March", "April",
          "May", "June", "July", "August",
          "September", "October", "November", "December"]
result = slice_list(months)
print(result)