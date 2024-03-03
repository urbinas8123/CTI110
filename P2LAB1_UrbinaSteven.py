#Steven Urbina
#March 2nd 2024
#P2LAB1
#Writing a program with a car's gas mileage (miles/gallon) and the cost of gas (dollars/gallon) as floating-point input, and output the gas cost for 20 miles, 75 miles, and 500 miles.







mileage = float(input())
cost_per_gallon = float(input())





gas_cost_20_miles = (20/ mileage) * cost_per_gallon
gas_cost_75_miles = (75/ mileage ) * cost_per_gallon
gas_cost_500_miles = (500/ mileage ) * cost_per_gallon

print(f'{gas_cost_20_miles:.2f} {gas_cost_75_miles:.2f} {gas_cost_500_miles:.2f}')
