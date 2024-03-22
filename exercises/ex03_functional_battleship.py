"""EX03 - Battleship."""

__author__ = "730704805"
import random

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


def input_guess(size: int, side: str) -> int:
    """This function is responsible for taking the row and column input. It uses a while loop to continue to ask the user to guess a row/column until they chose a value within the grid size. It takes a second argument."""
    assert side == "row" or side == "column"
    guess_row: int = int(input(f"Guess a {side}: "))
    while guess_row < 1 or guess_row > size:
        guess_row = int(input(f"The grid is only {size} by {size}. Try again: "))
    return guess_row


def print_grid(size: int, grow: int, gcolumn: int, corguess: bool) -> None:
    """This function prints a visualisation of the grid for the user. It takes the size of the grid, the guessed row, the guessed column, and whether the guess was correct as parameters. It uses 2 while loops to draw each row individually and checks for the guess coordinates drawing a white or blue square depending on if the user guessed correctly."""
    box: str = WHITE_BOX
    if corguess:
        box = RED_BOX

    grid_x: int = 1
    grid_y: int = 1
    while grid_y <= size:
        grid_x = 1
        crow: str = ""
        while grid_x <= size:
            if grow == grid_y and gcolumn == grid_x:
                crow += box
            else:
                crow += BLUE_BOX
            grid_x += 1
        print(crow)
        grid_y += 1
    if not corguess:
        print("Miss!")
    

def correct_guess(srow: int, scolumn: int, grow: int, gcolumn: int) -> bool:
    """This function checks if the user guessed correctly."""
    return (srow == grow and scolumn == gcolumn)


def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """The main function controls the game loop. It sets up a while loop that continues to prompt the user to guess a coordinate until the guess correctly or have had 5 turns."""
    turn = 0
    out = False
    while not out:
        turn = turn + 1
        print(f"=== Turn {turn}/5 ===")
        row_guess = input_guess(grid_size, "row")
        column_guess = input_guess(grid_size, "column")
        print_grid(grid_size, row_guess, column_guess, correct_guess(secret_row, secret_column, row_guess, column_guess))
        out = correct_guess(secret_row, secret_column, row_guess, column_guess) or turn == 5
    if turn < 5:
        print("Hit!")
        print(f"You won in {turn}/5 turns!")
    else:
        print("X/5 - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))