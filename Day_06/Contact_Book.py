

Contacts = []

total_contacts = int(input("How many Contacts Do you want to enter 🔢: "))

for i in range(total_contacts):

    print(f"\n Enter details for contact {i+1} : ")

    name = input("Enter Name 🔤 : ")
    phone = input("Enter phone number 🔢 : ")

    contact = {

          "Name": name,

          "Phone": phone
    }

    Contacts.append(contact)


print("\n === Search Contacts 🔎 ===")

search_name = input("\n Enter Contact Name 🔤 : ").strip()

found = False 

for contact in Contacts:

    if contact["Name"].lower() == search_name.lower():

        print("Phone : ", contact["Phone"])
        found = True
        break


