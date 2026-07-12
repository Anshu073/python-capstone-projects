operator = input("Enter an operator (+ - * /): ")
a = float(input("Enter the 1st number: "))
b = float(input("Enter the 2nd number: "))

if operator == "+":
    result = a + b
    print(f"Addition of {a} & {b} is: {result}")
elif operator == "-":
    result = a - b
    print(f"ASubtraction of {a} & {b} is: {result}")
elif operator == "*":
    result = a * b
    print(f"Multiplication of {a} & {b} is: {result}")
elif operator == "/":
    if a == 0:
        print(f"We cannot divide 0 by any number!")
    else:
        result = a / b
        print(f"Division of {a} & {b} is: {round(result,3)}")
else:
    print(f"{operator} is not valid operator!")