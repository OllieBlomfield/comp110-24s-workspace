"""EX03 - Better Battleship"""

__author__ = "730704805"

def input_guess(size: int,side: str) -> int:
    guess_row: int = int(input(f"Guess a {side}: "))
    while guess_row < 0 and guess_row>size:
        guess_row = int(input(f"The grid is only {size} by {size}. Try again: "))
    return guess_row

def print_grid(size: int, grow: int, gcolumn: int, corguess: bool):
    box: str = "\U00002B1C" 
    if corguess: box = "\U0001F7E5"
    for y in range(size): 
        crow: str = ""
        for x in range(size):
            if grow==y+1 and gcolumn==x+1: crow+=box
            else: crow+="\U0001F7E6"
        print(crow)
    if not corguess: print("Miss!")

def main(grid_size: int, secret_row: int, secret_column: int):
    turn=0
    out=False
    while not out:
        turn+=1
        print(f"=== Turn {turn}/5 ===")
        row_guess = input_guess(grid_size,"row")
        column_guess = input_guess(grid_size,"column")
        print_grid(grid_size,row_guess,column_guess, secret_column==column_guess and secret_row==row_guess)
        out = (secret_column==column_guess and secret_row==row_guess) or turn==5
    if turn<5: print(f"Hit!\nYou won in {turn}/5 turns!")
    else: print("X/6 - Better luck next time!")

main(4,3,2)