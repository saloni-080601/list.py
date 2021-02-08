# i=1
# while i<=5:
#     j=1
#     while j<=5:
#         print("*",end=" ")
#         j+=1
#     print()
#     i+=1
    
row=1
i=0
j=4
while i<=7:
    column=1
    while column<=5:
        if column==1 or (row==column+2 and column>1):
            print("*",end="")
        elif ((row==i and column==j) and column>0):
            print("*",end="")
        column+=1
    i+=1
    j-=1
        
    print()        
    row+=1


    