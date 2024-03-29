import pygame
import sys
import math
import random
pygame.init
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
running = True
tree_locations_y = []
tree_locations_x = []
tree_colors_tru = []
tree_colors = ['darkgoldenrod1','darkgoldenrod2', 'darkgoldenrod3', 'darkgoldenrod4', 'darkorange', 'darkorange1', 'darkorange2', 'darkorange3', 'darkorange4', 'firebrick', 'firebrick1', 'firebrick2', 'firebrick3', 'firebrick4']
for x in range(25000):
    random_value_y = random.randint(250,720)
    random_value_x = random.randint(0,1280)
    tree_locations_y.append(random_value_y)
    tree_locations_x.append(random_value_x)
for x in range(25000):
    tree_colors_tru.append(tree_colors[random.randint(0,13)])
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill("cyan")
    #drawing clouds
    pygame.draw.ellipse(screen,'grey90',pygame.Rect(200,60,500,150))
    pygame.draw.ellipse(screen,'grey90',pygame.Rect(250,100,500,150))
    #drawing the ground
    pygame.draw.rect(screen,'brown',pygame.Rect(0,250,1280,720))
    
    for x in range(25000):
            pygame.draw.circle(screen,tree_colors_tru[x],(tree_locations_x[x],tree_locations_y[x]),tree_locations_y[x]/10)
            pygame.draw.circle(screen,tree_colors_tru[x],(tree_locations_x[x],tree_locations_y[x] + 50),tree_locations_y[x]/10)
    #Drawing the mountain cliff
    pygame.draw.polygon(screen,"grey",[(0,720),(200,520),(500,420),(640,300),(800,400),(1000,520),(1280,720)])
    #Drawing the sun
    pygame.draw.circle(screen,'yellow',(1280,0),200)
    pygame.draw.line(screen,'yellow',(1080,0),(800,100),20)
    pygame.draw.line(screen,'yellow',(1180,100),(900,300),20)
    pygame.draw.line(screen,'yellow',(1280,200),(1000,500),20)
    #drawing the stone on the cliff
    pygame.draw.ellipse(screen,'dimgrey',pygame.Rect(400,400,350,375))
    pygame.display.update()