"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__="730704805"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
def askguess():
    plrguess:int=int(input("Pick a secret boat location between 1 and 4: "))
    if plrguess<1:
        print("Error! " + str(plrguess) + " too low!")
        exit()
    elif plrguess>4:
        print("Error! " + str(plrguess) + " too high!")
        exit()
    else:
        return plrguess
    
def pout(box):
    finout=BLUE_BOX*4
    for i in range(4):
        if i+1==p2guess:
            finout[i]=box
    return finout

p1guess:int=askguess()
p2guess:int=askguess()
result:str=""
if p1guess==p2guess:
    print(pout(RED_BOX))
    print("Correct! You hit the ship.")
else:
    print(pout(WHITE_BOX))
    print("Incorrect! You missed the ship.")
