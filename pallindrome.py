#pallindrome
def pal(n):
    l=[]
    for i in n:
        l.append(i)
    l1=l[::-1]
    if l1==l:
        print(n,"is Pallidrome")
    else:
        print(n,"is not a pallidrome")
n=str(input("Enter a number :"))
pal(n)