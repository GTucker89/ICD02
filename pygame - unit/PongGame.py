import pygame
import sys
import math
import random
import time
pygame.init()
paddle_hit = pygame.mixer.Sound('C:\\Users\\GTucker\\ICD20.py\\pygame - unit\\mixkit-air-in-a-hit-2161.wav')
goal = pygame.mixer.Sound('C:\\Users\\GTucker\\ICD20.py\\pygame - unit\\mixkit-animated-small-group-applause-523.wav')
clock = pygame.time.Clock()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
font = pygame.font.SysFont(None,36)
running = True
paddle_one_x = 50
paddle_one_y = 300 
paddle_two_x = 925
paddle_two_y = 300
ball_x = 500
ball_y = 400
radius = 25
ball_up = True
paddle_one_control = True
player_one_score = 0
color = (255,255,255)
player_two_score = 0
ball_speed = .5
count = 1
while running:
    pygame.time.set_timer(10,1000)
    screen.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    win_text_one = font.render("Player One WINS!", True, 'white')
    win_text_two = font.render("Player Two WINS!", True, 'white')
    score_text_one = font.render(f"Player One Score: {int(player_one_score)}", True, 'white')
    screen.blit(score_text_one,(100,0))
    score_text_two = font.render(f"Player Two Score: {int(player_two_score)}", True, 'white')
    screen.blit(score_text_two,(SCREEN_WIDTH - 325, 0))

    pygame.draw.rect(screen,'blue1',pygame.Rect(paddle_one_x,paddle_one_y,25,100))
    pygame.draw.rect(screen,'red',pygame.Rect(paddle_two_x,paddle_two_y,25,100))

    paddle_one = pygame.Rect(paddle_one_x,paddle_one_y,25,100)
    paddle_two = pygame.Rect(paddle_two_x,paddle_two_y,25,100)

    pygame.draw.circle(screen,(255,255,255),(ball_x,ball_y),25)
    circle = {'rect': pygame.Rect(ball_x, ball_y, 2*radius, 2*radius), 'color': color, 'radius': radius}
    
    if ball_up == True:
        ball_y += 5
    if ball_up == False:
        ball_y -= 5
    if ball_y >= 775:
        ball_up = False
    if ball_y <= 25:
        ball_up = True
    if paddle_one_control == True:
        ball_x += 5
    if paddle_one_control == False:
        ball_x -= 5
    if ball_x >= 975:
        pygame.mixer.Sound.play(goal)
        player_one_score += 1
        ball_x = 500
        ball_y = 400
    if ball_x <= 25:
        pygame.mixer.Sound.play(goal)
        player_two_score += 1
        ball_x = 500
        ball_y = 400
    pygame.display.update()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        if paddle_one_y <= 700:
            paddle_one_y += 5
    if keys[pygame.K_w]:
        if paddle_one_y >=0:
            paddle_one_y -= 5
    if keys[pygame.K_DOWN]:
        if paddle_two_y <= 700:
            paddle_two_y += 5
    if keys[pygame.K_UP]:
        if paddle_two_y >= 0:
            paddle_two_y -= 5
    if running == True:
        if paddle_one.colliderect(circle['rect']):
            paddle_one_control = True
            pygame.mixer.Sound.play(paddle_hit)
            if ball_up == True:
                ball_up == False
            else:
                ball_up == True
        if paddle_two.colliderect(circle['rect']):
            pygame.mixer.Sound.play(paddle_hit)
            paddle_one_control = False
            if ball_up == True:
                ball_up == False
            else:
                ball_up == True
    if player_one_score == 5:
        screen.blit(win_text_one,(SCREEN_WIDTH//2,SCREEN_HEIGHT//2))
        pygame.display.update()
        time.sleep(5)
        pygame.quit()
        sys.exit()
    if player_two_score == 5:
        screen.blit(win_text_two,(SCREEN_WIDTH//2,SCREEN_HEIGHT//2))
        pygame.display.update()
        time.sleep(5)
        pygame.quit()
        sys.exit()
    if count == 1:
        count += 1
        time.sleep(5)
    clock.tick(60)
    