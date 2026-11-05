A = list(map(int, input().split()))
largest = A[0]
second = A[0]
for i in range(len(A)):
    if A[i] > largest:
        second = largest
        largest = A[i]
    else:
        if A[i] > second:
            second = A[i]
print("Second Largest:", largest)

