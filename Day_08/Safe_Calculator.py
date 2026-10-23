# Safe Multi-Operation Calculator with help of Error handling

def calculate(num1,num2,operation):
    if operation == "+":
        return num1+num2
    elif operation == "-":
        return num1-num2
    elif operation == "*":
        return num1*num2
    elif operation == "/":
        return num1/num2
    else:
        print("\n          Invalid operation!")

while True:
    print("\n        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")
    print("              ===== SAFE CALCULATOR =====")
    print("        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")

    print("          📢 Type 'EXIT' to Close ")
    operation = input("\n          Enter Operation (➕ , ➖ , ✖️ , ➗): ")
    if operation.lower() == "exit":
        print("\n          Calculator closed❗")
        break
    if operation not in ["+","-","/","*"]:
        print("          Invalid operation ❗")
        continue
    try:
        num1 =float(input("\n          Enter First Number 🔢 : "))
        num2 =float(input("\n          Enter Second Number 🔢 : "))
        if operation == "/" and num2 == 0:
            print("\n          Division can not be performed with Zero ❗")
            continue
        result = calculate(num1,num2,operation)
        print("\n          Result: ",result)
    except ValueError:
        print("\n          Enter a valid number ")
