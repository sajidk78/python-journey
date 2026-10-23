# Profile Card upgrade using File handling and Error handling

import json

FILE = "Profiles.json"

def load_profiles():
    try:
        with open(FILE,"r") as f:
            return json.load(f)
    except FileNotFoundError:
        return[]
    except json.JSONDecodeError:
        print("Profile.json invalid ,starting with imupty list")
        return[]

def save_profiles(Profiles):
    with open(FILE , "w") as f:
        json.dump(Profiles,f,indent=4)

def add_profile(Profiles):
    name = input("          ☞Enter Name: ")
    age = int(input("          ☞Enter Age: "))
    city = input("          ☞Enter City: ")
    goal = input("          ☞Enter Goal: ")
    try:
        age = int(age)
    except ValueError:
        age = None
    profile = {
              "Name":name,
              "Age":age,
              "City":city,
              "Goal":goal
              }
    Profiles.append(profile)
    save_profiles(Profiles)
    print("            Profile Saved Successfuly 🎉")

def show_profile(profile):
    print("\n        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")
    print("               ((((((( Profile Of ",profile["Name"]," )))))))")
    print("        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")
    print("\n           Name: ",profile["Name"].title())
    print("\n           Age: ",profile["Age"])
    print("\n           City: ",profile["City"].title())
    print("\n           Goal: ",profile["Goal"].title())


def search_profile(Profiles):
    search_name = input("           ☞Enter Name to search profile: ").lower()
    found = False
    for profile in Profiles:
        if search_name == profile["Name"].lower():
            show_profile(profile)
            found = True
        else:
            None

def show_all_profiles(Profiles):
    if not Profiles:
        print("\n           Not any profile is available !")
    for profile in Profiles:
        show_profile(profile)

Profiles = load_profiles()

def main():

    while True:
        print("\n        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")
        print("              ===== PROFILE SYSTEM ===== ")
        print("        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")

        print("\n               1⃣. ADD PROFILES. " )
        print("\n               2⃣. SEARCH PROFILE. " )
        print("\n               3⃣. ALL PROFILES. " )
        print("\n               4⃣. EXIT. " )

        choice = int(input("\n             ☞ Enter Choice: "))
        if choice == 1:
            print("\n        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")
            print("              ===== PROFILE DETAILS =====")
            print("        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")
            add_profile(Profiles)
        elif choice == 2:
            print("\n        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")
            print("               ===== SEARCH PROFILE ===== ")
            print("        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")
            search_profile(Profiles)
        elif choice == 3:
            print("\n        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")
            print("               ===== ALL PROFILES =====")
            print("        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")
            show_all_profiles(Profiles)
        elif choice == 4:
            print("\n             Program Closed !")
            break
       
main()
