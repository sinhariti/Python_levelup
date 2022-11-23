def prime_factorial(n):
    f=[]
    d=2
    while d<=n:
        if n%d==0:
            f.append(d)
            n=n//d
        else:
            d+=1
    print("The prime factors are :",f)
n=int(input("Enter a number :"))
prime_factorial(n)