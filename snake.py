import pygame
from random import randint
from sys import exit

pygame.init()
window = pygame.display.set_mode((800, 480))
pygame.display.set_caption('Snake-Python')
clock = pygame.time.Clock()
game_active = True

velocity = 16
x = 0
y = 0 

food = pygame.Rect(150, 150, 8, 8)
snakecoords = [[400, i*16 + 240] for i in range(0,3)]
snakelen = len(snakecoords)
pixel_font = pygame.font.Font('font/Pixeltype.ttf', 50)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    if game_active:
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
        
        if snakecoords[0][1] - y > 0 and snakecoords[0][1] + y < (480-16):
            pass
        else:
            game_active = False

        if snakecoords[0][0] - x > 0 and snakecoords[0][0] + x < (800-16):
            pass
        else:
            game_active = False
        
        print(f'{x}x, {y}y')

        window.fill((20, 20, 50))

        for i in range(snakelen-1,0,-1):
            snakecoords[i][0] = snakecoords[i-1][0]
            snakecoords[i][1] = snakecoords[i-1][1]

        snakecoords[0][0] += x
        snakecoords[0][1] += y

        [pygame.draw.rect(window, (0, 200, 100), pygame.Rect(snakecoords[i][0], snakecoords[i][1], 16, 16)) for i in range(0,snakelen)]
        
        print(snakecoords)

    else:
        window.fill((50, 20, 20))
        message = pixel_font.render('You lost at snake', False, (255, 255, 255))
        message_rect = message.get_rect(center = (400, 200))
        messagetwo = pixel_font.render('press space to start again', False, (255, 255, 255))
        messagetwo_rect = messagetwo.get_rect(center = (400, 250))
        window.blit(message, message_rect)
        window.blit(messagetwo, messagetwo_rect)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            snakecoords = [[400, i*16 + 240] for i in range(0,3)]
            game_active = True
    
    # draw to the screen
    pygame.display.update()
    clock.tick(16)
