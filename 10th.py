N = int(input("Enter a num:"))
for i in range(N):
    L = N % 10
D = i // 10
f = D // 10
F = f // 10
print("last Digit:",L)
print("First Digit:",F)