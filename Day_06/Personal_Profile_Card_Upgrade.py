

Profiles = []

Number_Profiles = int(input("Enter Number of profiles you want to generate 🔢 : "))

for i in range(Number_Profiles):
    print(f"\n✳️✳️✳️✳️✳️✳️ Enter Details for profile {i+1} ✳️✳️✳️✳️✳️✳️")

    Name = input("Enter Name : ")
    Age = int(input("Enter Age : "))
    City = input("Enter City : ")
    Goal = input("Enter Goal : ")


    profile={

        "Name" : Name,
        "Age"  : Age,
        "City" : City,
        "Goal" : Goal
    }

    Profiles.append(profile)

while True:
    print("\n ♦♦♦♦♦♦ PROFILE CARD SYSTEM ♦♦♦♦♦♦")

    print("\n1⃣.Search Profile  🔎" )
    print("\n2⃣.All Profiles  🗂 " )
    print("\n3⃣.Exit" )

    choice = input("Enter Choice(1-3): ")

    if choice == "1":

        search_profile = input("Enter Profile Name 🔤: ").strip()
        found=False
        for profile in Profiles:
            if search_profile.lower() == profile["Name"].lower():
                print("\n➖➖➖ Profile Found 🎉➖➖➖")
                for key,value in profile.items():
                    print(f"{key.title()}:{value}")
                    found=True
            if not found:
                print("Profile not found")

    elif choice == "2":
        if len(Profiles) == 0:
            print("\n No any profile")
        else:
            print("\n ✖️✖️✖️✖️ ALL PROFILES ✖️✖️✖️✖️")
            for profile_Number,profile in enumerate(Profiles,start=0):
                print(f"\n ✴️✴️✴️✴️ PROFILE {profile_Number+1} ✴️✴️✴️✴️")
                for key,value in profile.items():
                    print(f"{key.title()}:{value}")
    elif choice == "3":
        print("\n Program closed")
        break
    else:
        print("\n Invalid choice please enter 1,2 or 3")
