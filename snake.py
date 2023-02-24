import pygame
from sys import exit

pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

snakebody = pygame.Rect(300, 300, 32, 32)
velocity = 2
x = 0
y = 0 

food = pygame.Rect(150, 150, 20, 20)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]: # right
        y = 0
        x = -1 * velocity
    if keys[pygame.K_d]: # left
        y = 0
        x = velocity
    if keys[pygame.K_w]: # up
        y = -1 * velocity
        x = 0
    if keys[pygame.K_s]: # down
        y = velocity
        x = 0
    
    if snakebody.y - y > 0 and snakebody.y + y < (600-32):
        snakebody.y += y
    else:
        print("you hit the wall on y")

    if snakebody.x - x > 0 and snakebody.x + x < (600-32):
        snakebody.x += x
    else:
        print("you hit the wall on x")

    window.fill((20, 20, 20))
    pygame.draw.rect(window, (0, 200, 0), snakebody)
    pygame.display.flip()
    clock.tick(60)
