a = int(input())
b = int(input())
c = int(input())

a2 = a ** 2
b2 = b ** 2
c2 = c ** 2

if 1 <= a <= 150 and 1 <= b <= 150 and 1 <= c <= 150:
    if (a2 == b2 + c2) or (b2 == a2 + c2) or (c2 == a2 + b2):
        print("YES")
    else:
        print("NO")
