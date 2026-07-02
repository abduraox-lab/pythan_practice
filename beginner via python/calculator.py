
opreator = input("enter your opreator (+, -, *, /, ): ")
num1 = float(input("enter your first number: "))
num2 = float(input("enter your second number: "))

if opreator == "+":
    result = num1 + num2
    print(result)
elif opreator == "-":
    result = num1 - num2
    print(result)
elif opreator == "*":
    result = num1 * num2
    print(result)
elif opreator == "/":
    result = num1 / num2
    print(result)
else:
    print(f"{opreator} is not valid")