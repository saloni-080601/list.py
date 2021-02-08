print("1.add", "2.substraction" , "3.multiplication" , "4.division")
a=int(input("enter a number"))
b=int(input("enter a number"))
c=input("enter a number")
if c=="1":
    sum=a+b
elif c=="2":  
    sum=a-b
elif c=="3":
    sum=a*b
elif c=="4":
    sum=a/b
else:
    print("invalid")
i=0
while i<=sum:
    print(i)
    i+=1
    

    
    

