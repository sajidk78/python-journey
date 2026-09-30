# Shopping list manager 

shopping_list = []

print("\n ==== SHOPPING LIST MANAGER 🛒 ====")

print("\n Type 'done' when completed")

while True:

    item = input("\n Enter item 📝: ")
    if item.lower() == "done":
        break

    if item == "":
        print("\n Item Should not be emputy")
        continue
    shopping_list.append(item)

print("\n ===== FINAL SHOPPING LIST 📝 =====")

item_number = 1

for item in shopping_list:
    print(f"\n{item_number}.{item}")
    item_number += 1
print(f"\n Total list items {len(shopping_list)}")
