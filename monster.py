import pygame
import constants as c
import random
import animation

class Monster(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__('spider')
        self.game = game
        self.max_health = 110
        self.health = self.max_health
        self.attack = 0.4
        self.y_vel = 0
        self.normal_speed = 2
        self.velocity = self.normal_speed
        #self.image = pygame.image.load('assets/elyes.jpg').convert_alpha()
        #self.image = pygame.transform.rotozoom(self.image, 0, 0.3)
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 300
        self.midair = True
        self.acc = 0
        self.gravity = c.GRAVITY
        self.ground = c.GROUND_HEIGHT - self.image.get_height() + 55
        self.left_speed = self.velocity + self.game.player.velocity
        self.right_speed = self.velocity - self.game.player.velocity
        self.start_animation('loop')

    def repop(self):
        self.rect.x = 1280 + random.randint(0, 300)
        self.health = self.max_health
        self.velocity = random.randint(1, 3)

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.repop()

    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, c.GRAY, [self.rect.x + 15, self.rect.y - 25, self.max_health, 5])
        pygame.draw.rect(surface, c.RED, [self.rect.x + 15, self.rect.y - 25, self.health, 5])

    def attraction(self):
        if self.midair:
            self.acc += self.gravity
            if self.y_vel < c.MAX_Y_VEL:
                self.y_vel += self.acc
            self.rect.y += self.y_vel
        if self.rect.y > self.ground:
            self.rect.y = self.ground
            self.acc = 0
            self.y_vel = 0
            self.gravity = c.GRAVITY
            self.midair = False

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)
        if self.rect.x <= 0 - 150:
            self.repop()