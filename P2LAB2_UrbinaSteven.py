

#Steven Urbina
#March 2nd 2024
#P2LAB2
#Using a string formatting expression with conversion specifiers to output their product and their average as integers




num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

product = num1 * num2* num3* num4
average =(num1 + num2 + num3 + num4)/4

print(f'{product:.0f} {average:.0f}')


print(f'{product:.3f} {average:.3f}')
