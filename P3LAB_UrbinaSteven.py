#Steven Urbina

#March 17 2024

#P3LAB

#Making a program that takes a year and determines whether that year is a leap year.

#Step 1. Taking the year has a input.
#Step 2. Check if the year is divisble by 4.
#Step 3. If it is divisble by 4, go to step 4; otherwise, go to step 8
#Step 4. Check if the year is a century year(divisble by 100).
#Step 5. If it is century year, go to step 6; otherwise, go to step 7
#Step 6. Check if the century year is divisble by 400.
#Step 7. If it is divisble by 400, output "Leap year"; otherwise, output "Not a leap year"












def is_leap_year(year):

    if year % 4==0: 
        if year % 100==0:
            if year % 400==0:
                return True
                
            else: 
                return False 
        else:
            return True
    else:
        return False
        
year =int(input())  


if is_leap_year(year):
    print(year, "- leap year")
else:
    print(year, "- not a leap year")
        
        
