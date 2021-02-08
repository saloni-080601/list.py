n=int(input("enter a number"))
f=0
f1=1
i=0
while n>=i:
    fn=f(n-1)+f1(n-2)
    print(fn)
    i+=1
