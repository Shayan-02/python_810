correctNumber = 50

guess = int(input("enter your choice: "))

# if guess == correctNumber:
#     print("you win")
# else:
#     if correctNumber > guess:
#         print("enter higher number")
#     else:
#         print("enter lower number")

if guess == correctNumber:
    print("you win")
elif correctNumber > guess:
    print("enter higher number")
else:
    print("enter lower number")