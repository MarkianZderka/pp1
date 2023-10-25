pinCode = "0805"

attempts = 0  

while attempts < 3:
    enterPIN = input("Enter PIN code: ")
    if enterPIN == pinCode:
        print("PIN code is correct. Access granted.")
        break  
    else:
        attempts += 1
        print("Incorrect PIN. You have", 3 - attempts, "attempts remaining.")

if attempts == 3:
    print("Sorry, your payment card has been blocked.")

