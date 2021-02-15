import pygame
import constants as c


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, length):
        super().__init__()
        self.width = width
        self.length = length
        # self.image = pygame.image.load('assets/platform.png')
        # self.rect = self.image.get_rect()
        self.x = x
        self.y = y