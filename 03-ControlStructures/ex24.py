price1 = int(input("Enter previous price: "))
price2 = int(input("Enter current price: "))

discount = ((price1 - price2)/price1) * 100

if discount >= 10:
    print("Buy the product!!!")
    print(f"The discount is {discount}%")
else:
    print("It is not worth buying it now")
