print("place your order")
size=input("enter the size of pizza 's','m',or'l':")
addpepo=input("do you want to (y/n):")
addcheese=input("do you want (y/n):")
bill=0
if(size=="s"):
    bill+=15
    print(f"your total will be {bill} ")
elif(size=="m"):
    bill+=20
    print(f"your total will be {bill}")
else:
    bill+=25
    print(f"your total will be {bill}")



if(addpepo=="y"):
    if(size=='s'):
        bill+=2
    else:
        bill+=3


if(addcheese=="y"):
    bill+=2

    print(f"youw totol bill wouldbe {bill}")


