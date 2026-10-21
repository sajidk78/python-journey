# Ticket number checker using function in python 

def is_even(number):
    return number % 2 == 0

print("\n        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")
print("              ===== TICKET NUMBER CHECKER =====")
for count in range(3):
    print("        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")

    ticket = int(input("\n           Enter ticket number: ")) 
    if is_even(ticket): 
        print("\n           Ticket", ticket, "is EVEN.") 
    else: 
        print("\n           Ticket", ticket, "is ODD.")
print("\n        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")

