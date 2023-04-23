import math

def number_precision(N,n):
    return "{:.{}f}".format(N,n)

pi = int(input("Gimme the number of decimal places you want for pi: "))
e = int(input("Gimme the number of decimal places you want for e: "))

if pi > 20 or e >20:
    print("precion exceeds capacity")
else:
    print(number_precision(math.pi,pi))
    print(number_precision(math.e,e))