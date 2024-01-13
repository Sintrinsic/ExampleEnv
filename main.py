# Initialize Pygame
import sys

import pygame

from game.character import Character

pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Centered Character Example')

# Create the character
character = Character('images/cato.jpg', screen)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the character
    screen.fill((0, 0, 0))  # Fill the screen with black
    character.display()  # Display the character

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()