n = int(input())

str_n = str(n)
reversed_n = ""

i = len(str_n) - 1

while i >= 0:
    reversed_n += str_n[i]
    i -= 1

# if reversed_n == str_n:
#     print("YES")
# else:
#     print("NO")

print("YES" if reversed_n == str_n else "NO")