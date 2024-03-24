#Steven Urbina

#March 24 2024

#P3HW2

#Create a program that calcuates how much a employee is going to make by their hours

#Step 1: Prompt the user to enter the employee's name
#Step 2: Prompt the user to enter the number of hours worked
#Step 3: Prompt the user to enter the pay rate
#Step 4: Check if the employee has worked overtime
#Step 5: Calculate the gross pay
#Step 6: Display the employee's information and gross pay 









employee_name=input("Enter employee's name:")
hours_worked=float(input("Enter number of hours worked:"))
pay_rate=float(input("Enter employee's pay rate:"))


if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = 40 * pay_rate
else:
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = hours_worked * pay_rate


gross_pay = regular_pay + overtime_pay

print("-----------------------------------------------------------------------------------------")
print("Employee Name:", employee_name)
print()
print("Hours Worked       Pay rate        Overtime    OverTime Pay    RegHour Pay    Gross Pay")
print("-----------------------------------------------------------------------------------------")

print(f"{hours_worked:<15.1f}{pay_rate:10.1f}{overtime_hours:15.1f}{overtime_pay:15.2f}{regular_pay:15.2f}{gross_pay:15.2f}")

