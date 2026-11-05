A = list(map(int, input().split()))
add = 0
Avg = 0
count = len(A)
for i in range(len(A)):
    add = add + A[i]

    if count > 0:
        Avg = add / count
print(add, Avg)