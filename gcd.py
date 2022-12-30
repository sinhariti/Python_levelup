a=int(input("Enter 1st num :"))
b=int(input("Enter 2nd num :"))
def gcd(a,b):
    if a>b:
        pass
    else: 
        a,b=b,a
    r=a%b
    while r!=0:
         a=b
         b=r
         r=a%b
    print ("GCD is :",b)
gcd(a,b)
