# Day_03
print("\n ===== Personal Profile Validation =====")


name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your City name: ").strip().title()
goal = input("Enter your goal: ").strip()

current_year = 2026

if age < 0 or age > 120:
    print("\n Invalid age.")
elif name == "":
    print("\n Name should not be empity")
else:
    name = name.strip().title()
    birth_year = current_year - age

print("\n ===== PROFILE CARD =====")

print(f"\n Name: {name}")
print(f"\n Age: {age}")
print(f"\n City: {city}")
print(f"\n Goal: {goal}")
print(f"\n Birth year: {birth_year}")
print(f"\n Next year you will be {age+1} years old")
