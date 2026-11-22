a = input()


reversed_a = ""
# for i in range(len(a) - 1, -1, -1):
#     reversed_a += a[i]

for i in a[::-1]:
    reversed_a += i

if reversed_a == a:
    print("yes")
else:
    print("no")