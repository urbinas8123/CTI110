    
#Steven Urbina

#April 28 2024

#P5HW

#Making a Math quiz program 





import random

def display_menu():
  
  print("""
  Welcome to Math Quiz

  MAIN MENU
  ----------------------

  1. Adding Random Numbers
  2. Subtracting Random Numbers
  3. Exit

  Please choose one of the menu options: """)

def generate_problem(operation):
  
  
  num1 = random.randint(100, 1000)
  num2 = random.randint(100, 1000)
  
  
  if operation == '+':
    problem = f"{num1} + {num2} = "
         
  else:
    
    if num1 < num2:
      num1, num2 = num2, num1
    problem = f"{num1} - {num2} = "
  
  
  answer = eval(problem[:-2])  

  return problem, answer  

def main():
  while True:
    display_menu()
    choice = input("> ")
    
    if choice in ('1', '2'):
      operation = '+' if choice == '1' else '-'
      problem, answer = generate_problem(operation)
      print(problem)
      num_guesses = 0  

      while True:  
        num_guesses += 1
        try:
          guess = int(input("Enter answer. "))
          if guess == answer:
            print(f"Congratulations!!!! Your answer is correct.")
            print(f"Number of guesses: {num_guesses}")
            break  
          elif guess < answer:  
            print("Sorry, guess is too low. Try again.")
            print()
          else:  
            print("Sorry, guess is too high.")
            print()
            print("Try again:")
        except ValueError:
          print("Invalid input. Please enter an integer.")
    elif choice == '3':
      print("Thank you for playing...")
      print("Bye!!!")
      break
    else:
      print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
  main()
