import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 800, 600
FPS = 30
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Pokemon Game")
clock = pygame.time.Clock()

# Pokemon class
class Pokemon(pygame.sprite.Sprite):
    def __init__(self, name, level):
        super().__init__()
        self.name = name
        self.level = level
        self.hp = level * 10
        self.attack = level * 2
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

# Player and opponent Pokemon
player_pokemon = Pokemon("Pikachu", 5)
opponent_pokemon = Pokemon("Charmander", 5)

# Create sprite groups
all_sprites = pygame.sprite.Group()
all_sprites.add(player_pokemon, opponent_pokemon)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player's turn
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        opponent_pokemon.take_damage(random.randint(1, player_pokemon.attack))

    # Opponent's turn
    player_pokemon.take_damage(random.randint(1, opponent_pokemon.attack))

    # Draw everything
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit the game
pygame.quit()
sys.exit()

