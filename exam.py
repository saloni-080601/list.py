# print("******wellcome*******")
#  card=input("insert your card:-")
lag=input("enter a language;-")
account=input("enter a account:-")
pin=int(input("enter your pin number:-"))
amount=int(input("enter your amount"))
balance=50000
if card=="pinside":
    if lag=="english"or"hindi"or"marathi":
        if account=="saving acoount"or"current":
            if pin== 1234:
                if balance<=50000:
                    print("succesfully")
                else:
                    print("money not sufficient")
            else:
                print("wrong pin number")
        else:
            print("not valid account")
    else:
        print("there is no language in system")
else:
    print("error")    
        