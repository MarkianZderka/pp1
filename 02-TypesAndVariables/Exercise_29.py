import random

attempt1 = random.randint(1, 6)
attempt2 = random.randint(1, 6)
attempt3 = random.randint(1, 6)

totalSum = attempt1 + attempt2 + attempt3

print(f"Results of three dice rolls {attempt1}, {attempt2}, {attempt3}")
print(f"Their sum is {totalSum}")
