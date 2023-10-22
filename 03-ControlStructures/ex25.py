numberOfProducts = int(input("Enter number of products: "))
priceOfProducts = int(input("Enter price of products: "))

totalAmountToPay = numberOfProducts * priceOfProducts

if numberOfProducts > 2:
    discount = ((numberOfProducts - 2) * priceOfProducts) * 0.75
    totalAmountToPay = 2 * priceOfProducts + discount
print(f"Amount to pay: {totalAmountToPay}")