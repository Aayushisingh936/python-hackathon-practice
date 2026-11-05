N = input("Enter a num:")
reverse = ""

for i in (N):
    reverse = i + reverse

if N == reverse:
    print("True")
else:
    print("False")