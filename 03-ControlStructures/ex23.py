ageInHumanYears = float(input("Enter dog`s age in human years: "))

ageInDogYears = ageInHumanYears * 10.5
if ageInHumanYears > 2:
    ageInDogYears = 21 + (ageInHumanYears - 2)*4

print(f"The dog's age in dog’s years is {ageInDogYears} years")