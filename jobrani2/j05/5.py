n = int(input("start: "))
m = int(input("end: "))

# for i in range(n , m+1):
#     if i % 3 == 0 and i % 5:
#         print(i)

i = n

while i <= m:
    if i % 3 == 0 and i % 5:
        print(i)
    i += 1


print("new start: ", n)