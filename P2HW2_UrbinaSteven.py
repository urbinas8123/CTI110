
#Steven Urbina

#March 10 2024

#P2HW2

#This program asks the user to enter grades for six modules, stores them in a list, and then displays the lowest grade, highest grade, sum of grades, and average grade

#Step 1. Create an empty list to store the grades.
#Step 2. Ask the user to enter the grade for each module separately.
#Step 3. Calculate the lowest grade in the list using the min() function.
#Step 4. Calculate the highest grade in the list using the max() function.
#Step 5. Calculate the sum of all grades using the sum() function.
#Step 6. Calculate the average grade by dividing the sum of grades by the total number of g
#Step 7. Display the lowest grade, highest grade, sum of grades, and average grade with appropriate formatting.







module_grades = []
module_names = ["Module 1", "Module 2", "Module 3", "Module 4", "Module 5", "Module 6"]

for i in range(1, 7):
    grade = float(input(f"Enter the grade for Module {i}: "))
    module_grades.append(grade)

lowest_grade = min(module_grades)
highest_grade = max(module_grades)
total_grades = sum(module_grades)
average_grade = total_grades / len(module_grades)

print()
print("\n------------How well did you do in school?------------")
print(f"Lowest Grade: \t{lowest_grade:}")
print(f"Highest Grade: \t{highest_grade:}")
print(f"Sum of Grades: \t{total_grades:}")
print(f"Average Grade: \t{average_grade:.2f}")
print("------------------------------------------")
