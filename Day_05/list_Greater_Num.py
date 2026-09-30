# find number Greater than 10 in a list

numbers = []

for i in range(5):

    number = int(input(f"\n Enter number {i+1}: "))
    numbers.append(number)

print("\n ==== Numbers Greater than 10 ====")

found = False

for number in numbers:

    if number > 10:
        print(number)
        found = True

if not found:
    print("\n No any number is greater than 10 found")

print (f"\n Total numbers {len(numbers)}")
print(f"\n All numbers {numbers}")
