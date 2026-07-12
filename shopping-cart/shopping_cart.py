# Shopping cart program

items = []
prices = []
total = 0

while True:
    item = input("Enter an item name (q to quit): ")
    if item.lower() == "q":
        break
    else:
        price = float(input(f"Enter a price of a {item}: $"))
        items.append(item)
        prices.append(price)

print("-------Your Cart-------")

print("List of total items:")
if not items:
    print("List is empty!")
else:
    for index in range(len(items)):
        print(f"{index+1}) {items[index]} (${prices[index]:.2f})")

print()
for price in prices:
    total += price

print(f"Your total is: ${total:.2f}")


