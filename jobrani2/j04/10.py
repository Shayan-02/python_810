# run = True
i = 0
sum_numbers = 0
while True:
    num = int(input(f"enter number{i+1}: "))
    if num == 0:
        break
        # run = False
    else:
        sum_numbers += num
        i += 1

print(f"sum of numbers: {sum_numbers}")
print(f"average of numbers: {sum_numbers/i}")