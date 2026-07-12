# Concession Stand Program

print("----- Menu -----")
menu = {
    "potato": 1.0,
    "chips": 2.0,
    "pepsi": 1.5,
    "soda": 2.5,
    "popcorn": 6.0
}

cart = []
total = 0

for key,value in menu.items():
    print(f"{key}: ${value}")

print("----------------")

while(True):
    food = input("Select an item (q to quit): ").lower()

    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print(f"{food} is not available in our menu! please select an available item")

print("----- Your Order -----")

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")

        
 



