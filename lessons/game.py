"""Number Guessing Game"""
from random import randint
SECRET: int = randint(0,int(input("Pick a range: ")))
guess=int(input("Guess the number: "))
while guess!=SECRET:
    print("Too High" if guess>SECRET else "Too Low")
    guess=int(input("Guess the number: "))
print("You Win!")