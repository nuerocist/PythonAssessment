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



