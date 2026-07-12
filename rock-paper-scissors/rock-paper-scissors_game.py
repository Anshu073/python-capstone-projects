# Rock-Paper-Scissors Game

import random

options = ("rock","paper","scissors")
playing = True

while playing:
    player = None
    computer = random.choice(options)    

    player = input("Enter a choice (rock,paper,scissors): ")

    while player not in options:
        print("Invalid choice!")
        player = input("Enter a choice (rock,paper,scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You Win.")
    elif player == "paper" and computer == "rock":
        print("You Win.")
    elif player == "scissors" and computer == "paper":
        print("You Win.")
    else:
        print("You Lose.")
    
    playing_again = input("Play again? (y/n): ").lower()
    if not playing_again == "y":
        if not playing_again == "n":
            print("Invalid choice!")
            input("Play again? (y/n): ").lower()
        else:
            playing = False
            
print("Thanks for playing...")

