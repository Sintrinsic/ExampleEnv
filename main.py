import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Centered Character Example')

# Load the character image
character = pygame.image.load('images/cato.jpg')
character = pygame.transform.scale(character, (40, 40))  # Scale the image to 40x40 pixels

# Get the rectangle of the image for positioning
character_rect = character.get_rect()
character_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the character
    screen.fill((0, 0, 0))  # Fill the screen with black
    screen.blit(character, character_rect)  # Draw the character image

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()