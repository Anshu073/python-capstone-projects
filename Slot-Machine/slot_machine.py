# Python Slot Machine Program
import random

def spin_row():
    symbols = ['🍒', '🍉', '🍊', '🔔 ', '⭐']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 2
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍊':
            return bet * 8
        elif row[0] == '🔔':
            return bet * 16
        elif row[0] == '⭐':
            return bet * 32
    return 0

def main():
    balance = 100
    isContinue = True

    print("**************************************")
    print("Welcome to python Slot machine program")
    print("Symbols: 🍒 🍉 🍊 🔔 ⭐")
    print("**************************************")
    
    while balance > 0:

        print(f"Your Balance: {balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Invalid number!")
            continue
        
        bet = int(bet)

        if bet > balance:
            print("Insufficient Funds")
            continue
        elif bet <= 0:
            print("Bet must be greater than 0!")
            continue
        
        balance -= bet

        row = spin_row()
        
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row,bet)
        if payout > 0:
            print(f"You won ${payout} 😃")
        else:
            print("Sorry you lost this round! 😔")

        balance += payout

        bet_again = input("Want to bet again? (Y/N): ").upper()
        if not bet_again == 'Y':
            if balance != 0:
                print(f"Your current balance: {balance}")
            break
    
    if balance == 0:
        if bet_again == 'Y':
            print("Unable to play!")
        print(f"Your current balance: ${balance}")


if __name__ == "__main__":
    main()