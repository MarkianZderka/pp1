price = float(input("Enter the price: "))
discount = float(input("Enter the discount: ")) * 0.01


disountedPrice = price * (1.0 - discount)

totalDiscount = price - disountedPrice

formattedDiscountedPrice = "{:.2f}".format(disountedPrice)
formattedTotalDiscount = "{:.2f}".format(totalDiscount)

print(f"Price with disount: {formattedDiscountedPrice}")
print(f"Reduction: {formattedTotalDiscount}")