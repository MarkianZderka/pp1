import random

attempt1 = random.randint(1, 6)
isSpecialnumber = True
if 2 <= attempt1 <= 5:
    isSpecialnumber = False

print(f"Your dice rolled {attempt1}")
print(f"Is is special number {isSpecialnumber}")    