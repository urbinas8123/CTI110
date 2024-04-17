#Steven Urbina

#April 14 2024

#P4HW1

#Create a program using a loop and displaying the score average and the letter grade of the calcuated average.

#Step 1. Prompt the user to enter the number of scores
#Step 2. Collect the scores
#Step 3. Find the lowest score
#Step 4. Remove the lowest score from the list
#Step 5. Calculate the average of the modified list
#Step 6. Determien the letter grade
#Step 7. Display the results












scores = []

num_scores = int(input("How many scores do you want to enter? "))
print()
for i in range(1, num_scores + 1):
    while True:
        score = float(input(f"Enter score #{i}: "))
        if 0 <= score <= 100:
            scores.append(score)
            break
        else:
            print()
            print("INVALID Score entered!!!!")
            print("Score should be between 0 and 100")

lowest_score = min(scores)
modified_scores = [score for score in scores if score != lowest_score]
average = sum(modified_scores) / len(modified_scores)

if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

print()
print("\n----------------Results---------------------")
print(f"Lowest score  :\t{lowest_score:}")
print(f"Modified List :\t{modified_scores:}")
print(f"Scores Average:\t{average:.2f}")
print(f"Grade         :\t{grade:}")
print("------------------------------------------")
