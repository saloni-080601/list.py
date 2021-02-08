n=int(input("enter a number"))
i=n
count=0
while i>10:
    i=i//10
    count=count+1
    sum=0
    i=n
    while i>0:
        digit=i%10
        b=digit
        c=digit**count+b**count
        print(c)
if c==n:
    print("amstrong number")
else:
    print("not amstrong no.")


