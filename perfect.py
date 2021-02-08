num1=int(input("enter a no"))
i=1
f=0
while i<num1:
    if num1%i==0:
        print(i)
        f=f+i
    i+=1
if f==num1:
    print("it is perfect no:",f)
else:
    print("it is not perfect:",f)