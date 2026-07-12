# Compund interest calculator

#variables declares with intialization
principle = 0
rate = 0
time = 0

# For principle
while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than zero!")
    else:
        break

# For Rate of interest
while True:
    rate = float(input("Enter the rate of interest: "))
    if rate < 0:
        print("Rate of interest can't be less than zero!")
    else:
        break

#For periods of time
while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be less than zero!")
    else:
        break

# Formula of compund interest
total = principle * pow((1 + rate/100),time)

print(f"Balance after {time} years/s: ${total:.2f}")
