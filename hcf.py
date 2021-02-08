a=int(input("enter a number"))
b=int(input("enter a number"))
while a%b!=0:
    rem=a%b
    a=b
    b=rem
else:
    print(b)
