N = int(input("Enter a num:"))
if N > 1:
    for i in range (2, N):
        if N % i == 0:
            print(" Not Prime")
            break
    else:
        print("prime")
else:
    print("prime")