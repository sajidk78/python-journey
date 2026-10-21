# Square Area Calculator using functions in python

def calculate_area(side):
    return side * side

print("\n        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")
print("             ===== SQUARE AREA CALCULATOR ===== ")

for count in range(3):
    print("        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")
    side = float(input("\n        Enter Square side length: "))
    area = calculate_area(side)
    print("\n        Square Area: ",area)
print("\n        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")
