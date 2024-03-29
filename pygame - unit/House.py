import sys
import pygame
pygame.init()
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("House Drawing")
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)
YELLOW = (255, 255, 0)
while True:
    screen.fill(WHITE)  
    
    pygame.draw.rect(screen, BLUE, (150, 200, 200, 150)) 
    
    pygame.draw.polygon(screen, BROWN, [(150, 200), (250, 100), (350, 200)])
    
    pygame.draw.rect(screen, BROWN, (225, 280, 50, 70))
    
    pygame.draw.circle(screen, YELLOW, (200, 230), 20)  
    pygame.draw.circle(screen, YELLOW, (300, 230), 20)  
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
