A = list(map(int, input().split()))
countE = 0
countO = 0
for i in range (len(A)):
    if A[i] % 2 == 0:
        countE += 1
    else:
        countO += 1
print("ODD:",countO)
print("EVEN:",countE)