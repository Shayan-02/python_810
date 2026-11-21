a = int(input())
b = int(input())
c = int(input())

fis = False

a2 = a ** 2
b2 = b ** 2
c2 = c ** 2

if 1 <= a <= 150 and 1 <= b <= 150 and 1 <= c <= 150:
        if a2 == b2 + c2:
            fis = True
        elif b2 == a2 + c2:
            fis = True
        elif c2 == b2 + a2:
            fis = True


if fis:
    print("YES")
else:
    print("NO")
