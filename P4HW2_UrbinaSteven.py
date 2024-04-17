#Steven Urbina

#April 14 2024

#P4HW2

#Create a program that calculates gross pay for multiple employees

#Step 1.Initialize variables
#Step 2. Loop until user enters "Done"
#Step 3. Get pay rate and hours worked
#Step 4. Calculate overtime and regular pay
#Step 5. Calculate gross pay
#Step 6. Accumulate totals
#Step 7. Display individual results
#Step 8. Display final results










def calculate_payroll():
 

  
  total_overtime_pay = 0
  total_regular_pay = 0
  total_gross_pay = 0
  number_of_employees = 0

  
  while True:
    
    employee_name = input("Enter employee name or 'Done' to terminate: ")
    if employee_name == "Done":
      break

    
    try:
        hours_worked = float(input("How many hours did " + employee_name + " work? "))
        pay_rate = float(input("What is " + employee_name + " pay rate? "))
    except ValueError:
      print("Invalid input. Please enter numbers for pay rate and hours.")
      continue

    
    if hours_worked > 40:
      overtime_hours = hours_worked - 40
      overtime_pay = overtime_hours * (pay_rate * 1.5)
      regular_pay = 40 * pay_rate
    else:
      overtime_hours = 0
      overtime_pay = 0
      regular_pay = hours_worked * pay_rate

    
    gross_pay = overtime_pay + regular_pay

    
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    number_of_employees += 1

    
    print()
    print("Employee Name:", employee_name)
    print()
    print("Hours Worked       Pay rate        Overtime    OverTime Pay    RegHour Pay    Gross Pay")
    print("-----------------------------------------------------------------------------------------")

    print(f"{hours_worked:<15.1f}{pay_rate:10.1f}{overtime_hours:15.1f}{overtime_pay:15.2f}{regular_pay:15.2f}{gross_pay:15.2f}")
    print()
  
  print()
  print(f"Total number of employees entered: {number_of_employees}")
  print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
  print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
  print(f"Total amount paid in gross: ${total_gross_pay:.2f}")

calculate_payroll()
