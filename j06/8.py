for i in range(1, 20):
    if i == 17:
        break
    elif i == 7 or i == 13:
        # i -= 1
        continue
    print(i, end=" ")