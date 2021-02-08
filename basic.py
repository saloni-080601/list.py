a=15
b=11
c=10
if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is greater")
elif c>a and c>b:
    print("c is greater")
elif a==b:
    print("a is equal to b")
elif b==c:
    print("b is equal to c")
elif c==a:
    print("c is equal to a")
else:
    print("all are not equal")