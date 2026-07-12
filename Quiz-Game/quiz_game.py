# Quiz game

questions = (
    "What is the capital of india?: ",
    "What is the capital of maharashtra?: ",
    "What is the capital of karnataka?: ",
    "What is the capital of rajasthan?: ",
    "What is the capital of gujarat?: "
)

options = (
    ("A) Mumbai","B) New delhi","C) Kolkata","D) Chennai"),
    ("A) Pune","B) Nagpur","C) Mumbai","D) Nashik"),
    ("A) Mystore","B) Bengaluru","C) Hubli","D) Mangalore"),
    ("A) Udaipur","B) Jodhpur","C) Jaipur","D) Kota"),
    ("A) Ahmedabad","B) Surat","C) Vadodara","D) Gandhinagar")
)

answers = ("B","C","B","C","D")
guesses = []
score = 0
que_num = 0
valid_options = ("A","B","C","D")

while que_num < len(questions):
    print("--------------------------------------")
    print(questions[que_num])
    for option in options[que_num]:
        print(option)
    
    guess = input("Enter (A, B, C, D): ").upper()

    if guess not in valid_options:
        print("Invalid choice!Please enter a valid choice")

    else:
        guesses.append(guess)
        
        if guess == answers[que_num]:
            score += 1
            print("Correct!")
        else:
            print("Incorrect!")
            print(f"{answers[que_num]} is the correct answer")

        que_num += 1

print("--------------------")
print("      Results       ")
print("--------------------")

print("Answers: ",end="")
for answer in answers:
    print(answer,end=" ")
print()

print("Guesses: ",end="")
for guess in guesses:
    print(guess,end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")


