"""
t <= 0 -> ice
0 < t < 100 -> water
t >= 100 -> steam
"""

t = int(input("enter temp: "))

if t <= 0: 
    print("ice")
elif 0 < t < 100:
    print("water")
# elif t >= 100:
else:
    print("steam")