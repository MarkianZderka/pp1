money = int(input("Enter the amount in PLN: "))

coin5zl = 0
coin2zl = 0
coin1zl = 0

while money > 0:
    if money >= 5:
        coin5zl += 1
        money -= 5
    elif money >= 2:
        coin2zl += 1
        money -= 2
    else:
        coin1zl += 1
        money -= 1

print(f"The amount of PLN {money} in coins:")
print(f"5 zł – {coin5zl}")
print(f"2 zł – {coin2zl}")
print(f"1 zł – {coin1zl}")