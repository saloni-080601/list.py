guess=8
i=1
while i<=5:
    num=int(input("enter a number"))
    if num==guess:
        print("it is right")
        break
    else:  
        print("try again")
    i+=1
else:
    print("your chance finihsed")
