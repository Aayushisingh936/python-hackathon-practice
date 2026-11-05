A = list(map(int, input().split()))
countP = 0
countN = 0
countZ = 0
for i in range(len(A)):
    if A[i] > 0:
        countP += 1
    elif A[i] < 0:
        countN += 1
    else:
        countZ += 1
print("Positive:", countP)
print("Negative:", countN)
print("Zero:", countZ)