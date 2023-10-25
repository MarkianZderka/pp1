sum_of_numbers = 0
count_of_numbers = 0

while True:
    number = int(input("Enter number: "))

    if number == 0:
        break  

    sum_of_numbers += number
    count_of_numbers += 1


if count_of_numbers > 0:
    mean = sum_of_numbers / count_of_numbers
else:
    mean = 0


print(f"RESULT: Quantity={count_of_numbers}, Sum={sum_of_numbers}, Mean={mean}")
