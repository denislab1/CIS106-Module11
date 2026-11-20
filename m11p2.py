
def calculate_scores(score1, score2, score3):
    total = score1 + score2 + score3
    average = total / 3
    return total, average


last_name = input("Enter student's last name: ")
score1 = float(input("Enter exam 1 score: "))
score2 = float(input("Enter exam 2 score: "))
score3 = float(input("Enter exam 3 score: "))

total, average = calculate_scores(score1, score2, score3)

print("Student:", last_name)
print("Total points:", total)
print("Average score:", round(average, 2))