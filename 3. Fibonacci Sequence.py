import time

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

nterms = int(input("How many terms do you want?: "))

if nterms<=0:
    print("Please enter a positive number")
else:
    for i in range(nterms):
        print(fibonacci(i))
        time.sleep(0.5)