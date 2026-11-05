A = list(map(int, input().split()))
reverse = []
for i in range(len(A)):
    reverse = [A[i]] + reverse
print(reverse)