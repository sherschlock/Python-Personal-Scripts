response = input("Do you want a prime number? y/n : ")

flag = 0
next_prime = 2
while response == "y":
    print(next_prime, end=" ")
    while True:
        flag=0
        next_prime += 1
        for i in range(2,next_prime):
            while next_prime%i==0:
                flag = 1
                break
        if flag == 0:
            break
    response = input("Do you want another prime number? y/n : ")