# weight=input("enter the weight")
# height=input("enter the height")
# weight_as_int=int(weight)
# height_as_float=float(height)
# BMI=weight_as_int/height_as_float ** 2
# Bmi_as_int=int(BMI)
# print(Bmi_as_int)


# print(type(9//5))

# score=12
# print("your score is " + str(score))
# print(f"your score is {score}") # use of f string

# ca=56  #BMI Calculation
# TA=90-ca
# twiam=int(4.34)
# twiay=int(52.14)
# totalWL=TA*twiay
# print(f"you have {totalWL} weeks left")

total_bill=float(input("enter the total bill: "))
print(type(total_bill))
tips=int(input("enter the tips (10,12 or 15: "))
total_bill_split=int(input("enter the number of people we splitting bill with: "))
total_for_each=total_bill*(tips/100)
final=(total_for_each+total_bill)/total_bill_split
print(f"the total amount for each person is {final}")

total_bill = float(input("Enter the total bill: "))
tips = int(input("Enter the tips (10, 12, or 15): "))
total_bill_split = int(input("Enter the number of people we are splitting the bill with: "))

total_for_each = total_bill * (tips / 100)
final = (total_for_each + total_bill) / total_bill_split

print(f"The total amount for each person is {final}")
