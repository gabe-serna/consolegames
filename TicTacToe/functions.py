board = []
for i in range(3):
    row = []
    for j in range(3):
        row.append("_")
    board.append(row)

def checkCorner(SCREEN_WIDTH, SCREEN_HEIGHT,counter):
    import pygame
    pos = pygame.mouse.get_pos()
    if pos[0] < SCREEN_WIDTH/3:
        # Left
        x = 60
        col = 0
    elif pos[0] > SCREEN_WIDTH/3 * 2:
        # Right
        x = 600
        col = 2
    else:
        # Middle
        x = 320
        col = 1

    if pos[1] < SCREEN_HEIGHT/3:
        # Top
        y = 25
        row = 0
        if updateBoard(row, col, counter):
            return x, y
        else:
            return -1, -1
    elif pos[1] > SCREEN_HEIGHT/3 * 2:
        # Bottom
        y = 420
        row = 2
        if updateBoard(row, col, counter):
            return x, y
        else:
            return -1, -1
    else:
        # Middle
        y = 230
        row = 1
        if updateBoard(row, col, counter):
            return x, y
        else:
            return -1, -1


def updateBoard(row,col,counter):
    global board
    if board[row][col] == "X" or board[row][col] == "O":
        return False
    else:
        if counter % 2 == 0:
            board[row][col] = 'X'
        else:
            board[row][col] = 'O'
        return True

def checkIfWin():
    global board
    if board[0][0] == board[0][1] == board[0][2] != "_":
        # Top Row
        return 0
    elif board[1][0] == board[1][1] == board[1][2] != "_":
        # Middle Row
        return 1
    elif board[2][0] == board[2][1] == board[2][2] != "_":
        # Bottom Row
        return 2
    elif board[0][0] == board[1][0] == board[2][0] != "_":
        # Left Col
        return 3
    elif board[0][1] == board[1][1] == board[2][1] != "_":
        # Middle Col
        return 4
    elif board[0][2] == board[1][2] == board[2][2] != "_":
        # Right Col
        return 5
    elif board[0][0] == board[1][1] == board[2][2] != "_":
        # Left Diagonal
        return 6
    elif board[0][2] == board[1][1] == board[2][0] != "_":
        # Right Diagonal
        return 7
    else:
        if checkIfLost():
            return -2
        else:
            return -1

def checkIfLost():
    global board
    if any("_" in row for row in board):
        return False
    else:
        return True

def gameWin(winState):
    if winState == 0:
        # Top Row
        start = (45, 100)
        end = (760, 100)
        return start, end
    if winState == 1:
        # Middle Row
        start = (45, 305)
        end = (760, 305)
        return start, end
    if winState == 2:
        # Bottom Row
        start = (45, 495)
        end = (760, 495)
        return start, end
    if winState == 3:
        # Left Col
        start = (135, 10)
        end = (135, 590)
        return start, end
    if winState == 4:
        # Middle Col
        start = (395, 10)
        end = (395, 590)
        return start, end
    if winState == 5:
        # Right Col
        start = (675, 10)
        end = (675, 590)
        return start, end
    if winState == 6:
        # Left Diagonal
        start = (55, 20)
        end = (780, 590)
        return start, end
    if winState == 7:
        # Right Diagonal
        start = (780, 20)
        end = (10, 590)
        return start, end
