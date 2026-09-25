# Day_04

print("\n === Multiple Profile Generator ===")

current_year = 2026

Number_of_profiles = int(input("Enter number of profiles you want to generate: "))

for profile_number in range (1,Number_of_profiles + 1):


    print(f"\n ==== PROFILE {profile_number} ====")

    Name = input("\n Enter your name: ")
    Age = int(input("\n Enter your age: "))
    City = input("\n Enter your city: ")
    Goal = input("\n Enter your goal: ")

    if Age <= 0 or Age >= 120:
        print("\n Invalid Age !")

    elif Name == "":
        print("\n Name should not be empity!")

    else:
        Name = Name.strip().title()
        Birth_year = current_year - Age

        print(f"\n Name: {Name}")
        print(f"\n Age: {Age}")
        print(f"\n City: {City}")
        print(f"\n Goal: {Goal}")
        print(f"\n Birth year: {Birth_year}")
        print(f"\n Next year you will be {Age + 1} years old")
