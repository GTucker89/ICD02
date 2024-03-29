import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
running = True
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Cyan = (0, 255, 255)
Magenta = (255, 0, 255)
Yellow = (255, 255, 0)
Black = (0, 0, 0)
White = (255, 255, 255)
Orange = (255, 165, 0)
Purple = (128, 0, 128)
Pink = (255, 192, 203)
Brown = (165, 42, 42)
Teal = (0, 128, 128)
Lime = (0, 255, 0)
Maroon = (128, 0, 0)
Navy = (0, 0, 128)
Olive = (128, 128, 0)
Turquoise = (64, 224, 208)
Indigo = (75, 0, 130)
Lavender = (230, 230, 250)
Beige = (245, 245, 220)
Salmon = (250, 128, 114)
SkyBlue = (135, 206, 235)
Silver = (192, 192, 192)
while running:
    screen.fill(White)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #Drawing the house
    pygame.draw.rect(screen,Brown,pygame.Rect(100,320,400,400))
    pygame.draw.rect(screen,SkyBlue,pygame.Rect(150,420,50,50))
    pygame.draw.rect(screen,SkyBlue,pygame.Rect(400,420,50,50))
    pygame.draw.rect(screen,Indigo,pygame.Rect(250,520,100,400))
    pygame.draw.polygon(screen,Maroon,[(100,320), (300,120),(500,320)])
    #Drawing the car
    pygame.draw.rect(screen,Silver,pygame.Rect(600,600,200,100))
    pygame.draw.circle(screen,Black,(600,700),20)
    pygame.draw.circle(screen,Black,(800,700),20)
    pygame.draw.rect(screen,SkyBlue,pygame.Rect(625,625,50,50))
    #Drawing on tree
    pygame.draw.rect(screen,Salmon,pygame.Rect(75,520,50,200))
    pygame.draw.polygon(screen,Olive,[(25,520),(100,300),(175,520)])
    pygame.draw.polygon(screen,Olive,[(25,420),(100,200),(175,420)])

    #Drawing on tree
    pygame.draw.rect(screen,Salmon,pygame.Rect(775,520,50,200))
    pygame.draw.polygon(screen,Olive,[(725,520),(800,300),(875,520)])
    pygame.draw.polygon(screen,Olive,[(725,420),(800,200),(875,420)])

    #Drawing sun
    pygame.draw.circle(screen,Yellow,(1000,250),100)
    
    #drawing stickman
    pygame.display.update()