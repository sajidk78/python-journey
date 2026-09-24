# Day_02 Profile Card updated

current_year = 2026

name = input("Enter your name: ").strip().title()
age = int(input("Enter your age: "))
city = input("Enter your city: ").strip().title()
goal = input("Enter your goal: ").strip().title()


print("\n ====PROFILE CARD====")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Goal: {goal}")
print(f"Next year you will be {age+1} years old")
