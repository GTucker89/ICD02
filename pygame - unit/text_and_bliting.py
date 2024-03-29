import pygame
import sys
screenw = 600
screenh = 600
pygame.init()
font1 = pygame.font.SysFont(None,24)
screen = pygame.display.set_mode((screenw,screenh))
clock = pygame.time.Clock()
time_remaining = 10
running = True
while running:
    screen.fill('white')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    text = font1.render(f"Hello, Pygame @ (25,25)! {int(time_remaining)}", True, 'red')
    text_rect = text.get_rect()
    clock.tick(60)
    screen.blit(text, (screenw // 2 - text.get_width() // 2,screenh // 2 - text.get_width()//2))
    time_remaining -= clock.get_time() / 1000
    if time_remaining <= 0:
        time_remaining = 0
        running = False
    pygame.display.update()