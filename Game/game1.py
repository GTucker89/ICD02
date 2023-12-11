import pygame as g
g.init()
from sys import *
import random

width = 750
height = 750
clock = g.time.Clock()
x = 0
y = 0

screen = g.display.set_mode((width, height))
g.display.set_caption('Snake')

f1x = 0
f1y = 0
follow1 = g.Surface((10, 10))
follow1.fill(('Red'))

test = g.Surface((10, 10))
test.fill((255, 0, 0))

applex = random.randint(0,74) * 10
appley = random.randint(0,74) * 10
apple = g.Surface((10,10))

test_x = 0
test_y = 0
u = 0
r = 0
speed = 10  # Adjust the speed as needed
# Initialize lists with a single element
previous_spacesx = [0,0,0,0,0,0,0]
previous_spacesy = [0,0,0,0,0,0,0]


while True:
    screen.fill((255, 255, 255))

    for event in g.event.get():
        if event.type == g.QUIT:
            g.quit()
            exit()

    keys = g.key.get_pressed()
    if keys[g.K_d]:
        if x == width - 10:
            x = width - 10
        elif r == -1:
            print("yes")
        else:
            r = 1
            u = 0
    elif keys[g.K_a]:
        if x == 0:
            x = 0
        elif r == 1:
            print("yes")
        else:
            r = -1
            u = 0
    elif keys[g.K_s]:
        if y == height - 10:
            y = height - 10
        elif u == -1:
            print("yes")
        else:
            u = 1
            r = 0
    elif keys[g.K_w]:
        if y == 0:
            y = 0
        elif u == 1:
            print("yes")
        else:
            u = -1
            r = 0
    for i in range(len(previous_spacesx) - 1, 0, -1):
         previous_spacesx[i] = previous_spacesx[i - 1]
         previous_spacesy[i] = previous_spacesy[i - 1]
         previous_spacesx[0] = x
         previous_spacesy[0] = y

    f1x = previous_spacesx[0]
    f1y = previous_spacesy[0]
    if r == 1:
        f1x = x
        f1y = y
        x += speed

    elif r == -1:
        f1x = x
        f1y = y
        x -= speed

    elif u == 1:
        f1x = x
        f1y = y
        y += speed
 
    elif u == -1:
        f1x = x
        f1y = y
        y -= speed
    
    

    # ...

    # Adjusting boundaries
    if test_y < 0:
        test_y = 0
    if test_x < 0:
        test_x = 0
    if test_y > height - 10:
        test_y = height - 10
    if test_x > width - 10:
        test_x = width - 10

    if x < 0:
        x = 0
    if y < 0:
        y = 0
    if y > height - 10:
        y = height - 10
    if x > width - 10:
        x = width - 10

    # Update the position of follow1 after boundary checks
        # Update the position of follow1 after boundary checks
    print(f"Body + {f1x,f1y}")
    print(f"head {test_x,test_y})" )
    screen.blit(follow1, (f1x, f1y))
    screen.blit(test, (test_x, test_y))
    screen.blit(apple, (applex, appley))

    # ...previous_spacesx = [3]

    g.display.update()
    clock.tick(1)
    g.time.delay(50)  # Introduce a delay to control the speed
