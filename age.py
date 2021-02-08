age=int(input("enter age"))
sex=input("enter the sex (M or f)")
maritalstatus=input("enter the marital status(m or not)")
if sex=="F":
    print("urban area")
elif sex=="M" and age>=20 and age<30:
    print("he is working anywhere")
elif sex=="M" and age>=30 and age<50:
    print("urban area")
else:
    print("Error")
