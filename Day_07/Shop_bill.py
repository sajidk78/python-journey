# Shop bill calculator using functions in python 

def shop_bill_calculate(price,quantity,discount=0):
    sub_total = price * quantity
    discount_amount = sub_total * discount/100
    return  sub_total - discount_amount

print("\n        ♦♦♦♦➖➖➖➖➖➖➖➖➖➖➖➖➖➖♦♦♦♦")
price = int(input("\n         ☞Item price: ")) 
quantity = int(input("\n         ☞Enter Quantity: "))
discount = float(input("\n         ☞Enter Discount(0 if not) %: "))

print("\n        ♦♦♦♦➖➖➖➖➖➖➖➖➖➖➖➖➖➖♦♦♦♦")
amount = shop_bill_calculate(price,quantity,discount)
print("\n         →Amount to pay: ",round(amount,2))
print("\n        ♦♦♦♦➖➖➖➖➖➖➖➖➖➖➖➖➖➖♦♦♦♦")
