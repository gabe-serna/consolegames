import sys
import pygame
import time
from functions import *

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
white = (255, 255, 255)
counter = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

surface = pygame.image.load("TicTacToe/cross.png").convert()
cross = pygame.transform.scale(surface, (150, 150))

surface2 = pygame.image.load("TicTacToe/circle.png").convert()
circle = pygame.transform.scale(surface2, (150, 150))

# cat
cat = pygame.image.load("TicTacToe/cat.png").convert()
cat = pygame.transform.rotozoom(cat, 0.5,3)
font = pygame.font.SysFont("Comic Sans", 45)
lose_title = font.render("THE CAT WINS", True, white)
horror_noises = pygame.mixer.Sound("TicTacToe/AHHHHHHH.mp3")

# Drawing the Gameboard
pygame.draw.line(screen, white, (266,0), (266, SCREEN_HEIGHT))
pygame.draw.line(screen, white, (533,0), (533, SCREEN_HEIGHT))
pygame.draw.line(screen, white, (0,200), (SCREEN_WIDTH, 200))
pygame.draw.line(screen, white, (0,400), (SCREEN_WIDTH, 400))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = checkCorner(SCREEN_WIDTH,SCREEN_HEIGHT,counter)
            if x != -1:
                if counter % 2 == 0:
                    screen.blit(cross, (x,y))
                else:
                    screen.blit(circle, (x,y))
                counter += 1
            winState = checkIfWin()
            if winState >= 0:
                start, end = gameWin(winState)
                pygame.draw.line(screen, white, start, end)
                pygame.display.flip()
                time.sleep(3)
                pygame.quit()
                sys.exit()
            elif winState == -2:
                # lose state
                screen.blit(cat, (0,0))
                screen.blit(lose_title, (50,50))
                horror_noises.play()
                pygame.display.flip()
                time.sleep(10)
                pygame.quit()
                sys.exit()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
