import pygame

class Character:
    def __init__(self, image_path, screen, size=(40, 40)):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        screen_width, screen_height = screen.get_size()
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.rect.center = (self.x, self.y)
        self.screen = screen

    def display(self):
        self.screen.blit(self.image, self.rect)

    def move(self, x, y):
        self.x += x
        self.y += y
        self.rect.center = (self.x, self.y)

