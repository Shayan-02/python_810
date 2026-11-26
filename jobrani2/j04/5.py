num1 = int(input("enter num1: "))
op = input("enter operator: ")
num2 = int(input("enter num2: "))

if op == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif op == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif op == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif op == "/":
    if num2 != 0:
        res = num1 / num2
        if res == int(res):
            print(f"{num1} / {num2} = {num1 // num2}")
        else:
            print(f"{num1} / {num2} = {res}")
    else:
        print("can't devide by zero")
else:
    print("enter valid operator (+ - * /)")