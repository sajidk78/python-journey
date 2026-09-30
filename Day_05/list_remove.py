# Remove duplicate items from the list

fruits = []

for i in range(5):
    fruit = input(f"\n Add fruit {i+1}: ")
    fruits.append(fruit)

print("\n === Original list ===")

print(f"\n{fruits}")

for fruit in fruits:
    print(f"\n{fruit}")
while True:
    fruit_to_remove = input("\n Enter fruit to remove: ").strip().lower()

    if fruit_to_remove in fruits:
        fruits.remove(fruit_to_remove)
        print(f"{fruit_to_remove} removed 🎉")

    else:
        print(f"\n {fruit_to_remove} not found")

    print(f"\n Final list {fruits}")

    if len(fruits) == 0:
        break
