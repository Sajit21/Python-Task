weight=int(input("enter your weight : "))
height=float(input("enter your height in meter: "))
bmi=weight/height ** 2
print(type(bmi))
print(bmi)
if(bmi<=18.5):
    print("your are underweight")
elif(18.5<bmi<25):
    print("your are normal weight")
elif(25<bmi<30):
    print("you are slightly overweight")
elif(30<bmi<35):
    print("you are obsse")
else:
    print("you are clinically obsse")
