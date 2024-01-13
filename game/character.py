import pygame

class Character:
    def __init__(self, image_path, screen, size=(40, 40)):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        screen_width, screen_height = screen.get_size()
        self.rect.center = (screen_width // 2, screen_height // 2)
        self.screen = screen

    def display(self):
        self.screen.blit(self.image, self.rect)