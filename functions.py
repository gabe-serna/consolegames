import random
import sys
import keyboard
score = 0

def game_start():
    global game_board
    game_board = [
        ['_','_','_','_'],
        ['_','_','_','_'],
        ['_','_','_','_'],
        ['_','_','_','_']
    ]
    x1 = random.randint(0,3)
    y1 = random.randint(0,3)
    x2 = random.randint(0, 3)
    while x2 == x1:
        x2 = random.randint(0,3)
    y2 = random.randint(0,3)

    game_board[x1][x2] = 2
    game_board[x2][y2] = 2
    print_board()

def print_board():
    for row in game_board:
        live_row = "  ".join(map(str,row))
        print(live_row)

#----------------------------------------------------------------
def on_up():
    i = 1
    while i <= 3:
        move_board_up()
        i += 1
    print("")
    add_new_number()
    print_board()

def move_board_up():
    row = 1
    while row <= 3:
        column = 0
        while column <= 3:
            number = game_board[row][column]
            reference = game_board[row - 1][column]
            move_number_up(number, reference, row, column)
            column += 1
        row += 1
    return game_board

def move_number_up(number, reference, row, column):
    if reference == '_':
        game_board[row - 1][column] = number
        game_board[row][column] = '_'
    elif reference == number:
        game_board[row - 1][column] = number * 2
        game_board[row][column] = '_'
        global score
        score += number * 2

#----------------------------------------------------------------
def on_down():
    i = 1
    while i <= 3:
        move_board_down()
        i += 1
    print("\n")
    add_new_number()
    print_board()

def move_board_down():
    row = 3
    while row >= 1:
        column = 0
        while column <= 3:
            number = game_board[row - 1][column]
            reference = game_board[row][column]
            move_number_down(number, reference, row, column)
            column += 1
        row -= 1
    return game_board

def move_number_down(number, reference, row, column):
    if reference == '_':
        game_board[row][column] = number
        game_board[row - 1][column] = '_'
    elif reference == number:
        game_board[row][column] = number * 2
        game_board[row - 1 ][column] = '_'
        global score
        score += number * 2

#----------------------------------------------------------------
def on_right():
    i = 1
    while i <= 3:
        move_board_right()
        i += 1
    print("\n")
    add_new_number()
    print_board()

def move_board_right():
    column = 2
    while column >= 0:
        row = 0
        while row <= 3:
            number = game_board[row][column]
            reference = game_board[row][column + 1]
            move_number_right(number, reference, row, column)
            row += 1
        column -= 1
    return game_board

def move_number_right(number, reference, row, column):
    if reference == '_':
        game_board[row][column + 1] = number
        game_board[row][column] = '_'
    elif reference == number:
        game_board[row][column + 1] = number * 2
        game_board[row][column] = '_'
        global score
        score += number * 2

#----------------------------------------------------------------
def on_left():
    i = 1
    while i <= 3:
        move_board_left()
        i += 1
    print("\n")
    add_new_number()
    print_board()

def move_board_left():
    column = 1
    while column <= 3:
        row = 0
        while row <= 3:
            number = game_board[row][column]
            reference = game_board[row][column -1]
            move_number_left(number, reference, row, column)
            row += 1
        column += 1
    return game_board

def move_number_left(number, reference, row, column):
    if reference == '_':
        game_board[row][column - 1] = number
        game_board[row][column] = '_'
    elif reference == number:
        game_board[row][column - 1] = number * 2
        game_board[row][column] = '_'
        global score
        score += number * 2

#----------------------------------------------------------------
def add_new_number():
    x = random.randint(0, 3)
    y = random.randint(0, 3)
    if any('_' in row for row in game_board):
        while game_board[x][y] != '_':
            x = random.randint(0, 3)
            y = random.randint(0, 3)
        game_board[x][y] = 2
    else:
        print(f"GAME OVER\nYou lost with a score of {score}")
        sys.exit()
