n = int(input("Enter the number: "))

for i in range(2,n+1):
    while n%i==0:
        print(i, end=" ")
        n = n/i