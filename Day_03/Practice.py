# Day 03 Independent practice

print("\n 1_=== Positive ,Negative or Zero===")

Number = float(input("\nEnter a number: "))

if Number < 0:
    print("\n Number is Negative.")

elif Number > 0:
    print("\n Number is Positive.")
else:
    print("\n Number is Zero.")



print("\n 2_ ==== Marks Grade ====")

marks = float(input("Enter marks (0-100): "))

if marks >= 90:
    print("A")

elif marks >= 70:
    print("B")

elif marks >= 60:
    print("C")

else:
    print("Fail")
