A = list(map(int, input().split()))
maximum = A[0]
minimum = A[0]
for i in range(len(A)):
    if A[i] > maximum:
        maximum = A[i]

    if A[i] < minimum:
        minimum = A[i]
print("Maximum:", maximum)
print("Minimum:", minimum)
