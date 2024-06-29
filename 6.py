print("Place your order")

size = input("Enter the size of pizza 's', 'm', or 'l': ")
add_pepperoni = input("Do you want to add pepperoni? 'y' or 'n': ")
add_cheese = input("Do you want to add extra cheese? 'y' or 'n': ")

bill = 0

if size == "s":
    bill += 15
    print(f"Your total will be {bill}")
elif size == "m":
    bill += 20
    print(f"Your total will be {bill}")
else:
    bill += 25
    print(f"Your total will be {bill}")

if add_pepperoni == 'y':
    if size == 's':
        bill += 2
    else:
        bill += 3

if add_cheese == 'y':
    bill += 2

print(f"Your total bill would be {bill}")
