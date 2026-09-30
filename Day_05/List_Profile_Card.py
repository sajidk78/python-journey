# Day_05 Store multiple profiles in a list

current_year = 2026

profiles =[]

Number_of_profiles = int(input("Enter Number of profiles you want to create: "))

for profile_number in range(1,Number_of_profiles+1):

    name = input("\n Enter your name 🔤: ")
    Age = int(input("\n Enter your age 🔢: "))
    City = input("\n Enter your city 🌏: ")
    Goal = input("\n Enter your goal 🗽: ")

    if Age <= 0 or Age >= 120:
        print("\n Invalid age")
    elif name == "":
        print("\n Name should not be emputy")

    else:
        name = name.title()
        birth_year = current_year- Age
 
        print(f"Profile {profile_number} Saved 📩")

        profile =f"""

\n ===== profile{profile_number} =====

Name: {name}
Age: {Age}
City: {City}
Goal: {Goal}
Birth Year: {birth_year}
Next year you will be {Age+1} years old

"""

        profiles.append(profile)

print ("\n ==== Saved Profiles ==== ")

for profile in profiles:
    print(profile)

print(f"\n Number of Profiles:{len(profiles)}")


