# Python Banking Program

def view_balance(balance):
    print("*************************")
    print(f"Your Balance is: ${balance:.2f}")

def deposite(balance):
    amount = input("How much want to deposite? ")

    if not amount.isdigit():
        print("*************************")
        print("Invalid amount!")
        return 0
    elif float(amount) == 0:
        print("*************************")
        print("Amount must be greater than 0!")
        return 0
    else:
        balance += float(amount)
        print("*************************")
        print(f"${float(amount):.2f} was deposited to your account.")
        return balance

def withdraw(balance):
    amount = input("How much want to withdraw? ")

    if not amount.isdigit():
        print("*************************")
        print("Invalid amount!")
        return 0
    elif float(amount) > balance:
        print("*************************")
        print("Insufficient balance!")
        print("Please check your balance first.")
        return 0
    elif float(amount) == 0:
        print("*************************")
        print("Amount should be greater than 0!")
        return 0
    else:
        balance -= float(amount)
        print("*************************")
        print(f"${float(amount):.2f} was withdrawn to your account.")
        return balance

def main():
    balance = 0
    is_continue = True
    while is_continue:
        print("*************************")
        print("     Banking Program     ")
        print("*************************")

        print("*************************")
        print("1) View Balance")
        print("2) Deposite")
        print("3) Withdraw")
        print("4) Exit")
        print("*************************")

        ch = input("choose an option (1-4): ")

        if not ch.isdigit():
            print("*************************")
            print("Choice should be number!")
        elif int(ch) == 1:
            view_balance(balance)
        elif int(ch) == 2:
            return_val = deposite(balance)
            if return_val == 0:
                pass
            else:
                balance = return_val
        elif int(ch) == 3:
            return_val = withdraw(balance)
            if return_val == 0:
                pass
            else:
                balance = return_val
        elif int(ch) == 4:
            is_continue = False
        else:
            print("*************************")
            print("Invalid Choice!")

        print("Thank you!Have a nice day!")
        print("*************************")

if __name__ == "__main__":
    main()