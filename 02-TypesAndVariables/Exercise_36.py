bankBuys = float(input("Bank buys: "))
bankSells = float(input("Bank sells: "))

spread = bankSells - bankBuys

formattedSpread = "{:.4f}".format(spread)

print(f"The spread is: {formattedSpread}")