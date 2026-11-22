x = input("enter a word: ")

i = 0
while i < len(x):
    print(x[i]) 
    i += 1
    
print("-"*30)

j = len(x) - 1
while j >= 0:
    print(x[j])
    j -= 1