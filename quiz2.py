# Quiz 2
# GUI Based Quiz 

from easygui import *
import matplotlib.pyplot as plt
import pandas as pd

name = enterbox("Enter your name: ")
year_group = buttonbox("Select your year group:", choices=["7", "8", "9", "10", "11", "12", "13"])

# Check if the user is eligible to take the quiz
if int(year_group) < 8:
    msgbox("You are too young to take the quiz")
    exit()
else:
    msgbox("Welcome to the quiz")

# Initialize score
score = 0

# Quiz questions and answers
qa = {
    'NZ': 'WGTN',
    'AUS': 'CAN',
    'IND': 'NDL',
    'CN': 'BJNG'
}

# Loop through questions and provide button options for answers
for q in qa:
    msg = f"What is the capital of {q}?"
    ans = buttonbox(msg, choices=list(qa.values()))
    if ans == qa[q]:
        score += 1
        msgbox("Correct")
    else:
        msgbox("Incorrect")

# Display final score and percentage
msgbox(f"You scored: {score}")
percentage = (score / len(qa)) * 100
msgbox(f"Percentage: {percentage}%")


with open("scores.csv","a") as mock_scores_file:
    mock_scores_file.write(f"\n{name},{score}")
    df = pd.read_csv('scores.csv')
    colors = ["red", "green", "yellow", "purple", "orange"]
    df.plot(x = 'Name', y = 'Score', kind = 'bar', color = colors)
    plt.show()


# Inform the user that the CSV has been created
msgbox("Your score has been saved to 'scores.csv'.")
