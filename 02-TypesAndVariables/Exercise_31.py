import random

diceRoll = random.randint(1,6)

guess = int(input("Guess the number: "))

winOrLose = False
if guess == diceRoll:
   winOrLose = True

print(f"And your guess is {winOrLose}")