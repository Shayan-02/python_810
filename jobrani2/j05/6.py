user1_win = 0
user2_win = 0
n = int(input("how many matches: "))
i = n
while i > 0:
    print(f"round {n - i + 1}: ")
    user1 = input("user1 enter your choice (sang / kaghaz / gheichi) : ")
    user2 = input("user2 enter your choice (sang / kaghaz / gheichi) : ")
    if user1 == "sang" or user1 == "kaghaz" or user1 == "gheichi":
        if user2 == "sang" or user2 == "kaghaz" or user2 == "gheichi":
            if user1 == user2:
                print(f"user1 : {user1} \nuser2: {user2} \ndraw")
            elif (user1 == "sang" and user2 == "gheichi") or (user1 == "kaghaz" and user2 == "sang") or (user1 == "gheichi" and user2 == "kaghaz"):
                print(f"user1 : {user1} \nuser2: {user2} \nuser1 wins")
                user1_win += 1
            else:
                print(f"user1 : {user1} \nuser2: {user2} \nuser2 wins")
                user2_win += 1
            i -= 1
        else:
            print("user2 enter valid choice")
    else:
        print("user1 enter valid choice")

print(f"user1 : {user1_win} wins\nuser2 : {user2_win} wins\ndraw : {n - (user1_win + user2_win)}")

if user1_win > user2_win:
    print("user1 win the game")
elif user2_win > user1_win:
    print("user2 win the game")
else:
    print("game draw")