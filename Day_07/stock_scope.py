# Stock Counter using functions in python 

def add_stock(current_stock,recieved):
    current_stock = current_stock + recieved
    return current_stock

print("\n        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")

current_stock = int(input("\n           ↪️ Enter Current Stock: "))
recieved = int(input("\n           ↪️ Add Stock: "))
updated_stock = add_stock(current_stock,recieved)

print("\n        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖ ⚜️ ")
print("\n           ↪️ Current Stock: ",current_stock) 
print("\n           ↪️ Updated Stock: ",updated_stock)

print("\n        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")

