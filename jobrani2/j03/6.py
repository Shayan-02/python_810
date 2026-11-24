fname = input("enter your firstname: ")
lname = input("enter your lastname: ")

print("my firstname is:", fname, "my lastname is:", lname)
print("my fullname is:", fname, lname)

print(f"my firstname is: {fname} my lastname is: {lname}")
print(f"my fullname is {fname} {lname}")

print("my firstname is: {} my lastname is: {}".format(fname, lname))
print("my fullname is {} {}".format(fname, lname))