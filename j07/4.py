n = int(input())

str_n = str(n)
reversed_n = ""

for i in range(len(str_n) - 1, -1, -1):
    reversed_n += str_n[i]

# if reversed_n == str_n:
#     print("YES")
# else:
#     print("NO")

print("YES" if reversed_n == str_n else "NO")