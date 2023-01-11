s=int(input("Enter units of efforts :"))
h=s//3600
s=s%3600
m=s//60
s=s%60
print("Hours: %02d\nMinutes: %02d\nSeconds :%02d"%(h,m,s))
