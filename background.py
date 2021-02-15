import pygame
import platform
import constants as c
import functions as f


class Background(pygame.sprite.Sprite):
    def __init__(self, game, file_name, file_name2):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('assets/' + file_name + '.png')
        self.length = self.image.get_width()
        self.rect = self.image.get_rect()
        self.image2 = pygame.image.load('assets/' + file_name2 + '.png')
        self.length2 = self.image2.get_width()
        self.rect2 = self.image2.get_rect()
        # self.platforms = [platform.Platform()]
        # self.images = f.load_list('assets/') à remplir

    def move_left(self, player):
        if not self.game.check_collision(self.game.player, self.game.all_monsters) and player.canMove:
            self.rect.x -= self.game.player.velocity

    def move_right(self, player):
        if not self.game.check_collision(self.game.player, self.game.all_monsters) and player.canMove:
            self.rect.x += self.game.player.velocity

    def move_left2(self, player):
        if not self.game.check_collision(self.game.player, self.game.all_monsters):
            self.rect2.x -= self.game.player.velocity/3

    def move_right2(self, player):
        if not self.game.check_collision(self.game.player, self.game.all_monsters):
            self.rect2.x += self.game.player.velocity/3




