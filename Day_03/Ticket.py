# Day 03

print("\n ==== Ticket Price Checker ====")

age = int(input(" Enter your age: "))

if age < 5:
    price = 0

elif age < 18:
    price = 200

else:
    price = 500

weekend = input("Is a weekend(yes/no): ")

if weekend == "yes":
    price = price + 50

print(f"\n Ticket price: {price}")

