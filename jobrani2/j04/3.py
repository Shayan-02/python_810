user1 = input("user1 enter your choice (sang / kaghaz / gheichi) : ")
user2 = input("user2 enter your choice (sang / kaghaz / gheichi) : ")

# way 1

# if user1 == "sang" and user2 == "sang":
#     print(f"user1 : {user1} \nuser2: {user2} \ndraw")
# elif user1 == "sang" and user2 == "kaghaz":
#     print(f"user1 : {user1} \nuser2: {user2} \nuser2 wins")
# elif user1 == "sang" and user2 == "gheichi":
#     print(f"user1 : {user1} \nuser2: {user2} \nuser1 wins")
# elif user1 == "kaghaz" and user2 == "kaghaz":
#     print(f"user1 : {user1} \nuser2: {user2} \ndraw")
# elif user1 == "kaghaz" and user2 == "gheichi":
#     print(f"user1 : {user1} \nuser2: {user2} \nuser2 wins")
# elif user1 == "kaghaz" and user2 == "sang":
#     print(f"user1 : {user1} \nuser2: {user2} \nuser1 wins")
# elif user1 == "gheichi" and user2 == "gheichi":
#     print(f"user1 : {user1} \nuser2: {user2} \ndraw")
# elif user1 == "gheichi" and user2 == "sang":
#     print(f"user1 : {user1} \nuser2: {user2} \nuser2 wins")
# elif user1 == "gheichi" and user2 == "kaghaz":
#     print(f"user1 : {user1} \nuser2: {user2} \nuser1 wins")

# way 2

# if (user1 == "sang" or user1 == "kaghaz" or user1 == "gheichi"):
#     if (user2 == "sang" or user2 == "kaghaz" or user2 == "gheichi"):
#         if user1 == user2:
#             print(f"user1 : {user1} \nuser2: {user2} \ndraw")
#         elif user1 == "sang" and user2 == "kaghaz":
#             print(f"user1 : {user1} \nuser2: {user2} \nuser2 wins")
#         elif user1 == "sang" and user2 == "gheichi":
#             print(f"user1 : {user1} \nuser2: {user2} \nuser1 wins")
#         elif user1 == "kaghaz" and user2 == "gheichi":
#             print(f"user1 : {user1} \nuser2: {user2} \nuser2 wins")
#         elif user1 == "kaghaz" and user2 == "sang":
#             print(f"user1 : {user1} \nuser2: {user2} \nuser1 wins")
#         elif user1 == "gheichi" and user2 == "sang":
#             print(f"user1 : {user1} \nuser2: {user2} \nuser2 wins")
#         elif user1 == "gheichi" and user2 == "kaghaz":
#             print(f"user1 : {user1} \nuser2: {user2} \nuser1 wins")
#     else:
#         print("user2 enter valid choice")
# else:
#     print("user1 enter valid choice")

# way 3

# if (user1 == "sang" or user1 == "kaghaz" or user1 == "gheichi"):
#     if (user2 == "sang" or user2 == "kaghaz" or user2 == "gheichi"):
#         if user1 == user2:
#             print(f"user1 : {user1} \nuser2: {user2} \ndraw")
#         elif user1 == "sang":
#             if user2 == "kaghaz":
#                 print(f"user1 : {user1} \nuser2: {user2} \nuser2 wins")
#             else:
#                 print(f"user1 : {user1} \nuser2: {user2} \nuser1 wins")
#         elif user1 == "kaghaz":
#             if user2 == "gheichi":
#                 print(f"user1 : {user1} \nuser2: {user2} \nuser2 wins")
#             else:
#                 print(f"user1 : {user1} \nuser2: {user2} \nuser1 wins")
#         elif user1 == "gheichi":
#             if user2 == "sang":
#                 print(f"user1 : {user1} \nuser2: {user2} \nuser2 wins")
#             else:
#                 print(f"user1 : {user1} \nuser2: {user2} \nuser1 wins")
#     else:
#         print("user2 enter valid choice")
# else:
#     print("user1 enter valid choice")

# way 4

if user1 == "sang" or user1 == "kaghaz" or user1 == "gheichi":
    if user2 == "sang" or user2 == "kaghaz" or user2 == "gheichi":
        if user1 == user2:
            print(f"user1 : {user1} \nuser2: {user2} \ndraw")
        elif (user1 == "sang" and user2 == "gheichi") or (user1 == "kaghaz" and user2 == "sang") or (user1 == "gheichi" and user2 == "kaghaz"):
            print(f"user1 : {user1} \nuser2: {user2} \nuser1 wins")
        else:
            print(f"user1 : {user1} \nuser2: {user2} \nuser2 wins")
    else:
        print("user2 enter valid choice")
else:
    print("user1 enter valid choice")