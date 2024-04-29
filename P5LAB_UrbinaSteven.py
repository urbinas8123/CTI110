def days_in_feb(user_year):
 


  if user_year % 4 == 0:  
    if user_year % 100 == 0 and user_year % 400 != 0:  
      return 28
    else:
      return 29
  else:
    return 28


user_year = int(input("Enter a year: "))


num_days = days_in_feb(user_year)
print(f"{user_year} has {num_days} days in February.")
