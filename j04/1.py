num = int(input("enter a number: "))

# way 1

if num == 0:
    print("zero")
else:
    if num % 2 == 0:
        print("even")
    else:
        print("odd")

print("-"*30)

# way 2

if num == 0:
    print("zero")
elif num % 2 == 0:
        print("even")
else:
    print("odd")
