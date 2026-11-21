a = int(input())
b = int(input())
c = int(input())

a2 = a ** 2
b2 = b ** 2
c2 = c** 2

if 1 <= a <= 150 and 1 <= b <= 150 and 1 <= c <= 150:
    if a > b and a > c:
        if a2 == b2 + c2:
            print("YES")
        else:
                print("NO")
    elif b > a and b > c:
        if b2 == a2 + c2:
                    print("YES")
        else:
                print("NO")
    elif c > b and c > a:
        if c2 == b2 + a2:
                    print("YES")
        else:
                print("NO")
    else:
        print("NO")