# Day_04 Independent practice

print ("\n (1)_ Print Numbers 1 to 20")

for i in range (1,21):
    print(i)



print("\n (ii)_ Print even numbers from 1 to 20")

for num in range (1,21):
    if num % 2 != 0:
        continue
    print(num)


print("\n (iii)_  Ask for numbers until 0")

while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        print("Done !")
        break

