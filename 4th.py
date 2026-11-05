N = int(input("Enter a num:"))
add = 0
for i in range(1, (N+1)):
    if i % 2 == 0:
        add = add + i
print(add)