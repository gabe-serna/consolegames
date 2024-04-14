import functions
import keyboard
from time import sleep
functions.game_start()

while not any(2048 in row for row in functions.game_board):
    sleep(0.5)
    key = keyboard.read_key()
    if key == 'up':
        functions.on_up()
    if key == 'down':
        functions.on_down()
    if key == 'right':
        functions.on_right()
    if key == 'left':
        functions.on_left()
    if key == 'enter':
        #this button makes you automatically win lol
        functions.game_board[0][0] = 2048
        functions.print_board()

print(f"You won with a score of {functions.score}")
sleep(1)
