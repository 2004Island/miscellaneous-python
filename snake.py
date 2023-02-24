import pygame
from sys import exit

pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
game_active = True

snakebody = pygame.Rect(300, 300, 32, 32)
velocity = 2
x = 0
y = 0 

food = pygame.Rect(150, 150, 20, 20)

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
        
        if snakebody.y - y > 0 and snakebody.y + y < (600-32):
            snakebody.y += y
        else:
            game_active = False

        if snakebody.x - x > 0 and snakebody.x + x < (600-32):
            snakebody.x += x
        else:
            game_active = False

        window.fill((20, 20, 50))
        pygame.draw.rect(window, (0, 200, 0), snakebody)
        
    else:
        window.fill((50, 20, 20))
        message = pixel_font.render('You lost at snake', False, (255, 255, 255))
        message_rect = message.get_rect(center = (300, 275))
        messagetwo = pixel_font.render('press space to start again', False, (255, 255, 255))
        messagetwo_rect = messagetwo.get_rect(center = (300, 325))
        window.blit(message, message_rect)
        window.blit(messagetwo, messagetwo_rect)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            snakebody.y = 300
            snakebody.x = 300
            game_active = True
    
    # draw to the screen
    pygame.display.update()
    clock.tick(60)
