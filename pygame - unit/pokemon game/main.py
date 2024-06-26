'''import pygame
import sys
import math

pygame.init()
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600

screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))
pygame.display.set_caption("Pokemon Demo")

running = True
while running:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running = False
    screen.fill((255,255,255))
    pygame.display.flip()

pygame.quit() '''


# Simple pygame program

# Import and initialize the pygame library
import sys
sys.path.append('C:\\Python312\\Lib\\site-packages')
import pygame
import math

pygame.init()
SCREEN_WIDTH = 1280
# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, 720])

# Run until the user asks to quit
running = True
x = 100
x_vel = 1
box_width = 50
radius = 30
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x, 0, box_width, 50))
    pygame.draw.circle(screen, (0, 255, 0), (x, 300), radius)
    pygame.draw.line(screen, (0, 0, 255), (0, 0), (800, 600), 20)
    pygame.draw.polygon(screen, (255, 255, 0), [(200, 200), (300, 300), (400, 200)])
    pygame.draw.arc(screen, (255, 0, 255), pygame.Rect(100, 100, 200, 200), 0, math.pi/2, 2)
    # pygame.draw.ellipse(screen, (0, 0, 255), pygame.Rect(200, 200, 200, 100))
    # pygame.draw.aaline(screen, (255, 0, 255), (0, 0), (800, 600))
    # pygame.draw.lines(screen, (100, 255, 0), False, [(100, 100), (200, 200), (300, 100)], 2)
    # x += x_vel

    if x > (SCREEN_WIDTH - radius) or x < radius:
        x_vel = -x_vel


    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
# Copilot
# raw.githubusercontent.com
# Ask a follow-up question
# GPT-3.5
# GPT-4

# Copilot is ready for this page
# Summary