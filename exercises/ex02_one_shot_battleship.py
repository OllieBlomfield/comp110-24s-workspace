"""EX02 - One Shot Battleship"""

__author__="730704805"

#Constants for the character codes for the blue, red and white box emojis.
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

#declares values of target location and grid size. All can be changed and program will still run fine as long as the secret row and column are kept within the grid size.
grid_size: int = 4
secret_row: int = 3
secret_column: int = 2

#This first while loop checks to make sure the user has inputed a value within the grid size for the row. It checks if the inputted value is in range and if it is it will set row_in_bounds to true, causing the while loop to end after it finishes that sequence. If the value isn't in bounds it prompts the user to input another value.
row_in_bounds: bool = False
guess_row: int = int(input("Guess a row: "))
while not row_in_bounds:
    if guess_row>0 and guess_row<=grid_size:
        row_in_bounds = True
    else:
        guess_row = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

#This second while loop uses identical logic to the previous but checks for the users column input.
column_in_bound: bool = False
guess_column: int = int(input("Guess a column: "))
while not column_in_bound:
    if guess_column>0 and guess_column<=grid_size:
        column_in_bound = True
    else:
        guess_column = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))


#This if statement checks to see if the user guessed correctly. If they did the colour of box is changed from white to red.
box: str = WHITE_BOX
if guess_column==secret_column and guess_row==secret_row:
    box=RED_BOX



#These two while loops mimic two for loops to display the grid. It uses two while loops, one iterates through the columns and the other through rows.
#Each row is printed individually. The variable crow is appended with either a blue box or a white/red box depending on if the box is in the location the player chose.
grid_x: int = 0
grid_y: int = 0
while grid_y<grid_size:
    grid_x=0
    crow: str = ""
    while grid_x<grid_size:
        if guess_row==grid_y+1 and guess_column==grid_x+1:
            crow+=box
        else:
            crow+=BLUE_BOX
        grid_x+=1
    print(crow)
    grid_y+=1


#These if/elif statements are used to determine which message should be displayed to the user after their guess. If they guess wrong but get the row/column correct, they are given a hint.
if guess_column==secret_column and guess_row==secret_row:
    print("Hit!")
elif guess_column==secret_column and guess_row!=secret_row:
    print("Close! Correct column, wrong row.")
elif guess_column!=secret_column and guess_row==secret_row:
    print("Close! Correct row, wrong column.")
else:
    print("Miss!")