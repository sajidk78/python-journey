# Day_04

print("\n(1) ===== For Loop =====")
 
for Number in range(1,10):
    print(f"Attempt: {Number}")


print("\n ==== For loop over a String ====")

for letter in "Python":
    print(letter)



print("\n(2) ==== While Loop ====")

Count = 0

while Count < 5:
    print(f"\n Count is:{Count}")
    Count +=1


print("\n ==== While loop for Validation ====")

password = input("Enter password (min 6 char): ")

while len(password) < 6:
    print("\n Too short,try again!")
    password = input("Enter password (min 6 char): ")

print("\n Password accepted ")


print("\n === Break & Continue ===")

for num in range (1,10):

   if num % 2 == 0:
       continue
   if num == 5:
       break

print(num)
