quantity=int(input("enter quantity"))
if quantity*100>1000:
    print((quantity*100)-((1*quantity*100)/100))
else:
    print(quantity*100)
age_12=int(input("enter first age"))
age_13=int(input("enter second age"))
age_15=int(input("enter third age"))
if age_12>=age_13 and age_12>=age_15:
    print("oldest")
if age_13>=age_12 and age_13>=age_15:
    print("oldest")
if age_15>=age_12 and age_15>=age_13:
    print("oldest")
else:
    print("youngest") 