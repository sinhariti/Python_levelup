n=int(input("Enter number of elements you want to add in the list :"))
a=[]
up=2
#creating the list
for k in range(0,n):
    ele=int(input("enter numbers :"))
    a.append(ele)
for u in range(1,n+1):
    end=len(a)-u
    for i in range (0,end):
        b=i
        c=i+up
        print(a[b:c],end=' ')
    up+=1
    print("")
'''for i in range(0,len(a)-2):
    b=i
    c=i+3
    print(a[b:c],end=" ")
print()
for i in range(0,len(a)-3):
    b=i
    c=i+4
    print(a[b:c],end=" ")
print()
print(a)'''
