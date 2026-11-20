
def calculate_average(score1, score2, score3, handicap):
    average = (score1 + score2 + score3) / 3
    average_handicap = average + handicap
    return average, average_handicap


last_name = input("Enter bowler's last name: ")
score1 = int(input("Enter game 1 score: "))
score2 = int(input("Enter game 2 score: "))
score3 = int(input("Enter game 3 score: "))
handicap = int(input("Enter handicap: "))

average, average_handicap = calculate_average(score1, score2, score3, handicap)

print("Bowler:", last_name)
print("Average score:", round(average, 2))
print("Average with handicap:", round(average_handicap, 2))
