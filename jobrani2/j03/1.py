temp = int(input("enter temprature: "))

# ----------- way 1 -------------

if temp <= 0:
    print("ice")
if 0 < temp < 100:
    print("water")
if temp >= 100:
    print("steam")

# ----------- way 2 -------------

if temp <= 0:
    print("ice")
else:
    if temp < 100:
        print("water")
    else:
        print("steam")

# ----------- way 3 -------------

if temp <= 0:
    print("ice")
elif temp < 100:
    print("water")
else:
    print("steam")