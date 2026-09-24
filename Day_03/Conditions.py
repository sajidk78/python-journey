# Day_03 Conditions

age =int(input("Enter your age: "))

if age < 0:
    print("\n Age can not be negative")
elif age < 13:
    print("\n You are a Child")
elif age < 20:
    print("\n You are teenager")
else:
    print("\n You are adult")


print("\n ===== ATM =====")

Amount = float(input("Enter your Amount: "))
Balance = 700
Daily_limit = 1000

if Amount > Balance:
    print("\n Insufficient Balance.")

elif Amount > Daily_limit:
    print("\n Exceeds daily limit")
else:
    print("\n Here is your Cash")



print("\n ===== LOGIN =====")

username = input("Enter Username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("\n Login Successful")
else:
    print("\n Invalid Credentials")


