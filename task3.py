# age_of_student=int(input("enter your age: "))
# if(age_of_student>=18):
#     height_of_student=int(input("enter your heigh: "))
#     if(height_of_student>=170):
#         print("they can ride")
#     else:
#         print("they cannot ride")
# else:
#     print("they should be at least 18 years old")      

height=int(input("enter your height in cm: "))
if(height>165):
    print("they can ride the roller coster")
    age=int(input("enter your age: "))
    if(age<12):
        print("they will pay $5")
    elif(12<=age<=18):
        print("they will pay $7")
    else:
        print("they will pay $12")
else:
    print("they cannot ride roller coaster")
