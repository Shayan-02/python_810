i = 1
sum_numbers = 0
tedad = 0
while i <= 3:
    number = int(input(f"enter your grade{i}: "))
    if 0 <= number <= 20:
        sum_numbers += number
        tedad += 1
        i += 1
    else:
        print("enter number between 0 and 20")


avg = sum_numbers / tedad 
if avg >= 18:
    print(f"your average is {avg}\nyour grade is A")
elif avg >= 16:
    print(f"your average is {avg}\nyour grade is B")
elif avg >= 14:
    print(f"your average is {avg}\nyour grade is C")
elif avg >= 10:
    print(f"your average is {avg}\nyour grade is D")
else:
    print(f"your average is {avg}\nyour  failed")