import pygame as pg
from math import radians, sin, cos

# Initialize Pygame
pg.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
FOV = 60  # Field of View in degrees

# Colors
WHITE = (255, 255, 255)

# Initialize the screen
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Simple FPS')

# Player variables
player_x, player_y = WIDTH // 2, HEIGHT // 2
player_angle = 0

# Game loop
clock = pg.time.Clock()
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    keys = pg.key.get_pressed()

    # Move the player forward and backward
    if keys[pg.K_w]:
        player_x += 5 * cos(radians(player_angle))
        player_y -= 5 * sin(radians(player_angle))
    if keys[pg.K_s]:
        player_x -= 5 * cos(radians(player_angle))
        player_y += 5 * sin(radians(player_angle))

    # Rotate the player left and right
    if keys[pg.K_a]:
        player_angle = (player_angle - 5) % 360
    if keys[pg.K_d]:
        player_angle = (player_angle + 5) % 360

    # Draw everything
    screen.fill(WHITE)

    # Draw player
    pg.draw.circle(screen, (0, 0, 255), (int(player_x), int(player_y)), 5)

    # Draw player's view (a simple cone representing the FOV)
    pg.draw.polygon(screen, (200, 200, 200),
                    [(player_x, player_y)] +
                    [(player_x + 300 * cos(radians(player_angle + i)),
                      player_y - 300 * sin(radians(player_angle + i)))
                     for i in range(-FOV // 2, FOV // 2, 5)])

    pg.display.flip()
    clock.tick(FPS)
