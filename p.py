num1=int(input("enter a no"))
i=1
f=0
while i<=num1:
    if num1%i==0:
        print(i)
        f=f+1
    i+=1
if f==2:
    print("it is prime no")
else:
    print("it is not prime")

    