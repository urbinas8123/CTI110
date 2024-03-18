#Steven Urbina

#March 17 2024

#P3HW1

# This program takes a number grade , determines average and displays letter grade for average.

#Step 1. Enter grades for six modules
#Step 2. Add grades entered to a list
#Step 3. Determine lowest,highest,sum and average for grades
#Step 4. Determine letter grade for average
#Step 5. Determine if average is above or below 90, 80, 70, 60 or 59 and then print correct description.

mod_1 = float(input('Enter grade for Module 1:'))
mod_2 = float(input('Enter grade for Module 2:'))
mod_3 = float(input('Enter grade for Module 3:'))
mod_4 = float(input('Enter grade for Module 4:'))
mod_5 = float(input('Enter grade for Module 5:'))
mod_6 = float(input('Enter grade for Module 6:'))



grades =[mod_1,mod_2,mod_3,mod_4,mod_5,mod_6]


low = min(grades)
high = max(grades)
sum_grades = sum(grades)
average = sum_grades / len(grades)


print()
print("\n------------Results------------")
print(f"Lowest Grade: \t{low:}")
print(f"Highest Grade: \t{high:}")
print(f"Sum of Grades: \t{sum_grades:}")
print(f"Average: \t{average:.2f}")
print("------------------------------------------")


if average >= 90:
    print('Your grade is: A')

elif average >= 80:
     print('Your grade is: B')

elif average >= 70:
    print('Your grade is: C')

elif average == 60:
     print('Your grade is: D')

else:
    print('Your grade is: F')





