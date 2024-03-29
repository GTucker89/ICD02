import sys
import pygame
import math
pygame.init()
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Smiley Face Drawing")
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
while True:
    screen.fill(WHITE) 
    
    pygame.draw.circle(screen, YELLOW, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), 150)
    
    pygame.draw.circle(screen, BLACK, (150, 150), 20)
    pygame.draw.circle(screen, BLACK, (250, 150), 20)
    
    pygame.draw.arc(screen, BLACK, (100, 155, 200, 125), math.pi, 2 * math.pi, 6)
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
