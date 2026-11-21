counter = int(input("enter count of numbers: "))
i = counter

sum_numbers = 0
while i >= 1:
    number = int(input("enter a number: "))
    sum_numbers += number
    i -= 1

print(sum_numbers/counter)
