import pygame
from sys import exit

pygame.init()

window = pygame.display.set_mode((600, 600))

pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    window.fill((0, 0, 0))
    pygame.display.update()
    clock.tick(60)
