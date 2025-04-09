# Quiz 1
# Terminal Based Quiz

name = input("Enter your name: ")
year_group = int(input("Enter your year group: "))
if year_group < 8:
    print("You are too young to take the quiz")
    exit()
else:
    print("Welcome to the quiz")
632,
score = 0

qa = {
    'NZ': 'WGTN',
    'AUS': 'CAN',
    'IND': 'NDL',
    'CN': 'BJNG'}

for q in qa:
    print(q)
    ans = input("Enter the capital of the country: ")
    if ans == qa[q]:
        score += 1  
        print("Correct")
    else:
        print("Incorrect")
print("You scored: ", score)

# Calculate the percentage
percentage = (score / 4) * 100
print("Percentage: ", percentage)



