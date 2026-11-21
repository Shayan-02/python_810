num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))

sum_numbers = num1 + num2
sub_numbers = num1 - num2
mul_numbers = num1 * num2
div_numbers = num1 / num2

# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)

print("------------- way 1 -------------")

print(num1, "+", num2, "=",  sum_numbers)
print(num1, "-", num2, "=",  sub_numbers)
print(num1, "*", num2, "=",  mul_numbers)
print(num1, "/", num2, "=",  div_numbers)

print("------------- way 2 -------------")

print(f"{num1} + {num2} = {sum_numbers}")
print(f"{num1} - {num2} = {sub_numbers}")
print(f"{num1} * {num2} = {mul_numbers}")
print(f"{num1} / {num2} = {div_numbers}")

print("------------- way 3 -------------")

print("{} + {} = {}".format(num1, num2, sum_numbers))
print("{} - {} = {}".format(num1, num2, sub_numbers))
print("{} * {} = {}".format(num1, num2, mul_numbers))
print("{} / {} = {}".format(num1, num2, div_numbers))
