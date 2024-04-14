import pygame
from pygame import Vector2
from random import randint

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
isDead = False

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.body = [Vector2(randint(1,31),randint(1,23))]
        self.image = pygame.surface.Surface((25, 25))
        self.rect = self.image.get_rect()
        self.direction = ''
        self.pause = 0
        self.eat = 0

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.direction = 'left'
        if keys[pygame.K_d]:
            self.direction = 'right'
        if keys[pygame.K_w]:
            self.direction = 'up'
        if keys[pygame.K_s]:
            self.direction = 'down'
        # Dev Testing (add length to snake by pressing E)
        # if keys[pygame.K_e]:
        #     self.eat = 1

    def movement(self):
        global new_head
        if self.direction != '':
            self.pause += 0.1
            if self.direction == 'up':
                if self.pause >= 1:
                    head_x = self.body[0][0]
                    head_y = self.body[0][1] - 1
                    new_head = Vector2(head_x, head_y)
                    self.appendNewHead(new_head)
                    self.pause = 0
            if self.direction == 'down':
                if self.pause >= 1:
                    head_x = self.body[0][0]
                    head_y = self.body[0][1] + 1
                    new_head = Vector2(head_x, head_y)
                    self.appendNewHead(new_head)
                    self.pause = 0
            if self.direction == 'left':
                if self.pause >= 1:
                    head_x = self.body[0][0] - 1
                    head_y = self.body[0][1]
                    new_head = Vector2(head_x, head_y)
                    self.appendNewHead(new_head)
                    self.pause = 0
            if self.direction == 'right':
                if self.pause >= 1:
                    head_x = self.body[0][0] + 1
                    head_y = self.body[0][1]
                    new_head = Vector2(head_x, head_y)
                    self.appendNewHead(new_head)
                    self.pause = 0

    def appendNewHead(self,new_head):
        # Check if Snake is moving into itself
        global isDead
        if new_head in self.body:
            isDead = True

        # Actually move the Snake
        if self.eat > 0: self.eat -= 1
        else: self.body.pop()
        self.body.insert(0, new_head)

    def drawSnake(self):
        for i in range(len(self.body)):
            x_pos = int(self.body[i][0] * 25)
            y_pos = int(self.body[i][1] * 25)
            snake_rect = pygame.Rect(x_pos,y_pos,25,25)
            if i == 0: color = (0,200,20)
            else: color = (0,255,0)
            pygame.draw.rect(screen,color,snake_rect)

    def checkIfHitWall(self):
        global isDead
        if self.body[0][0] < 0 or self.body[0][0] >= 32:
            print("Dead Wall")
            isDead = True
        elif self.body[0][1] < 0 or self.body[0][1] >= 24:
            print("Dead Wall")
            isDead = True

    def checkIfDead(self):
        if isDead: return True
        else: return False

    def update(self):
        self.input()
        self.movement()
        self.drawSnake()
        self.checkIfHitWall()

class Food:
    def __init__(self,x,y):
        self.body = [Vector2(x,y)]

    def drawFruit(self):
        x_pos = int(self.body[0][0] * 25)
        y_pos = int(self.body[0][1] * 25)
        fruit_rect = pygame.Rect(x_pos, y_pos, 25, 25)
        pygame.draw.rect(screen, (255,0,0), fruit_rect)
