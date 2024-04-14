from sys import exit
from time import sleep
from snake_classes import *

pygame.init()

def eat():
    global score
    for vector in player.body:
        if food.body[0] == vector:
            player.eat = 1
            score += 1

            # Adding a new Fruit and removing the old one
            x = randint(1, 28)
            y = randint(1, 20)
            while Vector2(x, y) in player.body:
                y = randint(1, 24)
            food.body.insert(0, Vector2(x, y))
            food.body.pop()


# Beginning Variables
font = pygame.font.Font('font/Pixeltype.ttf', 50)
clock = pygame.time.Clock()
score = 0

# Text
game_over = font.render('GAME OVER', False, (255, 255, 255))
game_over_rect = game_over.get_rect(center=(400, 50))

# Creating the Player
snake_group = pygame.sprite.Group()
player = Snake()
snake_group.add(player)

# Creating the First Food
food_x = randint(1, 28)
food_y = randint(1, 20)
while Vector2(food_x, food_y) in player.body:
    y = randint(1, 24)
food = Food(food_x,food_y)

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Score
    score_surf = font.render(f"Score: {score}", False, (50, 50, 50))
    score_rect = score_surf.get_rect(center=(700, 50))
    screen.blit(score_surf, score_rect)

    # Snake
    snake_group.draw(screen)
    snake_group.update()
    player.drawSnake()

    # Food
    food.drawFruit()

    # Collisions
    eat()

    if player.checkIfDead():
        screen.blit(game_over, game_over_rect)
        pygame.display.update(game_over_rect)
        sleep(2)
        pygame.quit()
        exit()

    pygame.display.flip()
    clock.tick(60)
