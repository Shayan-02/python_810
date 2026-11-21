user1 = input("""user1 enter your choice
1. sang 
2. kaghaz 
3. gheichi 
: """)

user2 = input("""user2 enter your choice
1. sang 
2. kaghaz 
3. gheichi 
: """)

if user1 == "sang" or user1 =="kaghaz" or user1 == "gheichi":
    if user2 == "sang" or user2 == "kaghaz" or user2 == "gheichi":
        if user1 == user2:
            print(f"user1 : {user1}\nuser2 : {user2}\ndraw")
        else:
            if user1 == "sang":
                if user2 == "kaghaz":
                    print(f"user1 : {user1}\nuser2 : {user2}\nwinner : user2")
                elif user2 == "gheichi":
                    print(f"user1 : {user1}\nuser2 : {user2}\nwinner : user1")
            elif user1 == "kaghaz":
                if user2 == "sang":
                    print(f"user1 : {user1}\nuser2 : {user2}\nwinner : user1")
                elif user2 == "gheichi":
                    print(f"user1 : {user1}\nuser2 : {user2}\nwinner : user2")
            elif user1 == "gheichi":
                if user2 == "sang":
                    print(f"user1 : {user1}\nuser2 : {user2}\nwinner : user2")
                elif user2 == "kaghaz":
                    print(f"user1 : {user1}\nuser2 : {user2}\nwinner : user1")
    else:
                print("user2 enter valid choice")
else:
                print("user1 enter valid choice")