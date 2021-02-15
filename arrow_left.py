import pygame


class ArrowLeft(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.normal_velocity = 10
        self.velocity = self.normal_velocity
        self.image = pygame.image.load('assets/Images/Arrow_150x150/Arrow_left.png')
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y
        self.player = player
        self.left_velocity = self.velocity - player.velocity
        self.right_velocity = self.velocity + player.velocity

    def remove(self):
        self.player.all_arrow.remove(self)

    def move(self):
        self.rect.x -= self.velocity
        # supprimer les fleches hors champ
        if self.rect.x < -150:
            self.remove()
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
            monster.damage(self.player.attack)