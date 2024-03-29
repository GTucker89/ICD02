import sys
import pygame
pygame.init()
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
color_1 = (255,0,75)
color_2 = (40,30,100)
color_3 = (50, 150, 75)
white = (255,255,255)
running = True
while running:
    screen.fill(white)
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(50,200,200,100))
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(55,205,50,50))
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(155,205,50,50))
    pygame.draw.circle(screen,(0,0,0), (50,300),20)
    pygame.draw.circle(screen,(0,0,0), (250,300),20)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()