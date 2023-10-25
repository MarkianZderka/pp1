import random

min_number = 5
max_number = 10

for _ in range(20):
    random_number = random.randint(min_number, max_number)
    print(random_number, end=" ")
