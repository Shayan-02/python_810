# start = int(input("enter start: "))
# end = int(input("enter end: "))

start = 10
end = 30

i = start

while i <= end:
    if i % 2 == 0:
        print(f"{i} -> even", end="\t")
    else:
        print(f"{i} -> odd", end="\t")
    i += 1
