c = 50
g = int(input("enter a guess: "))

if c == g:
    print("you win")
else:
    if c > g:
        print("enter bigger number")
    else:
        print("enter lower number")