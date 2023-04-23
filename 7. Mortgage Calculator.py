def mortgage(P,i,N):
    return P*i*(1+i)**N/((1+i)**N - 1)

P = float(input("How much loan do you want? : "))
i = float(input("What is the interest rate? : "))
N = float(input("What is the term? : "))
i = i/(100*12)
print(mortgage(P,i,N))