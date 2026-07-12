# Python Number Guessing Game

import random

lower_num = 1
higher_number= 100
guesses = 0
answer = random.randint(lower_num, higher_number)

print("---Number Guessing Game---")
print(f"Enter a select between {lower_num} and {higher_number}")

while True:
    guess = input("Enter a number: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lower_num or guess > higher_number:
            print("The selected number is out of range!")
            print(f"Please select a number between {lower_num} and {higher_number}")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Guess again!")
        else:
            print(f"Correct! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            break
    else:
        print("Invalid guess!")
        print(f"Please select a number between {lower_num} and {higher_number}")

