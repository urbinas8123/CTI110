#Steven Urbina

#Feb 25 2024

#P1HW2

#Creating a program using basic math and numbers

#Step 1:input initial budget, travel destination, gas cost, accommodation cost, and food cost

#Step 2: Calucate total expenses by gas_cost + accommodation_cost + food_cost

#Step 3: Calucate remaining balance by initial_budget - total_expenses 

#Step 4: Display the travel expenses breakdown 








print('This program calculates and displays travel expenses')
print()
initial_budget = float(input('Enter Budget:'))
print()
destination = input('Enter your travel destination:')
print()
gas_cost = float(input('How much do you think you will spend on gas?'))
print()
accommodation_cost = float(input('Approximately, how much will you need for accommodation/hotel?'))
print()
food_cost = float(input('Last, how much do you need for food?'))
print()
total_expenses = gas_cost + accommodation_cost + food_cost
remaining_balance = initial_budget - total_expenses
print("\n----------Travel Expenses---------")
print(f"Location:{destination}")
print(f"Initial Budget:${initial_budget}")
print()
print(f"Fuel:${gas_cost}")
print(f"Accommodation:${accommodation_cost}")
print(f"Food:${food_cost}")
print()
print(f"Remaining Balance:${remaining_balance}")
