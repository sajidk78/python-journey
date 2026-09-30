# list items deletation using pop()

nums = []

for i in range(5):
    number = int(input(f"\n Enter Number {i+1}: "))
    nums.append(number)

print(f"\n=== Original list of Numbers ==== \n{nums}")

for number in nums:
    print(number)

while True:
    pop_number = int(input("\n Enter index to remove the number at that: "))

    if pop_number == "":
        print("\n Number can not be emputy")
    else:
        rem_num = nums.pop(pop_number)

    print(f"\n Number {rem_num} is removed")
    print(f"\n Updated list {nums}")

    if len(nums) == 0:
        break

