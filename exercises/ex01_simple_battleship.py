"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730704805"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
 
p1guess: int = int(input("Pick a secret boat location between 1 and 4: "))
if p1guess < 1:
    print("Error! " + str(p1guess) + " too low!")
    exit()
elif p1guess > 4:
    print("Error! " + str(p1guess) + " too high!")
    exit()

    
p2guess: int = int(input("Guess a number between 1 and 4: "))
if p2guess < 1:
    print("Error! " + str(p2guess) + " too low!")
    exit()
elif p2guess > 4:
    print("Error! " + str(p2guess) + " too high!")
    exit()

result: str = ""
otherbox: str = ""
if p1guess == p2guess:
    otherbox = RED_BOX
else:
    otherbox = WHITE_BOX
    
counter: int = 1
if p2guess == counter:
    result += otherbox
else:
    result += BLUE_BOX
counter += 1
if p2guess == counter:
    result += otherbox
else:
    result += BLUE_BOX
counter += 1
if p2guess == counter:
    result += otherbox
else:
    result += BLUE_BOX
counter += 1
if p2guess == counter:
    result += otherbox
else:
    result += BLUE_BOX
print(result)
if otherbox == WHITE_BOX:
    print("Incorrect! You missed the ship.")
else:
    print("Correct! You hit the ship.")