# Profile Card updated using functions in python

def get_profile_input():
    name = input("\n             ↪️ Enter Name: ")
    age = int(input("\n            ↪️ Enter Age: "))
    city = input("\n            ↪️ Enter City name: ")
    goal = input("\n            ↪️ Enter Goal: ")

    try:
        age = int(age)
    except ValueError:
        age = None

    return {"Name":name , "Age":age , "City":city , "Goal":goal}
    

def validate_profile(profile):
    
    return(
         bool(profile["Name"])
         and profile["Age"]is not None
         and profile["Age"]> 0
         and bool(profile["City"])
         and bool(profile["Goal"]) 
         )

def print_profile(profile):
    print("\n        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")
    print("                 ===== PROFILE CARD =====  ")
    print("        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")
    print("\n          ☞ Name : ",profile["Name"].title().strip())
    print("\n          ☞ Age : ",profile["Age"])
    print("\n          ☞ City : ",profile["City"].title().strip())
    print("\n          ☞ Goal : ",profile["Goal"].title().strip())
    print("\n        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")

def show_all_profiles(profiles):
    if not profiles:
        print("\n          No any profile is added yet ❗")
        return
    for number , profile in enumerate(profiles , start = 1):
        print(f"\n              ------ PROFILE {number} ------")
        print_profile(profile)

def search_profile(profiles):
    search_name = input("\n          ↪️ Enter Name to Saerch: ").lower().strip()
    found = False
    for profile in profiles:
        if search_name in profile["Name"].lower().strip():
            print_profile(profile)
            found = True
    if not found:
        print("\n          Profile not found")

def main():
    profiles = []

    while True:
        print("\n        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")
        print("                ===== PROFILE RIGISTERY =====")
        print("        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")
        print("\n          1⃣. ADD PROFILE " )
        print("\n          2⃣. SHOW ALL PROFILES " )
        print("\n          3⃣. SEARCH PROFILE " )
        print("\n          4⃣. EXIT " )

        choice = int(input("\n          ↪️ Enter Choice (1-4): "))
        if choice == 1:
            print("\n        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")
            print("                ===== Enter Profile Details ===  ")
            print("        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")
            profile = get_profile_input()
            if validate_profile(profile):
                profiles.append(profile)
            else:
                print("          Invalid inputs")

        elif choice == 2:
            print("\n        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")
            print("                ===== All Profiles =====")
            print("        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")
            show_all_profiles(profiles)

        elif choice == 3:
            print("\n        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")
            print("                ===== Search Profile =====")
            print("        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")
            search_profile(profiles)
        
        elif choice == 4:
            print("\n          Program Closed")
            break
        else:
            print("\n          Invalid choice enter (1-4)")

main()

       
