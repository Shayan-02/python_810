i = 1
while i <= 20:
    if i == 17:
        break
    elif i == 7 or i == 13:
        i += 2
        continue
    print(i)
    i += 1