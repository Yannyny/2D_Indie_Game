import pygame
from player import Player
from monster import Monster
from platform import Platform
from background import Background
import constants as c
import functions as f


class Game:

    def __init__(self, background_name, background_name2):
        self.is_playing = False
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.all_platforms = pygame.sprite.Group() # à remplir
        self.background = Background(self, background_name, background_name2)

    def start(self):
        self.is_playing = True
        self.spawn_monster()

    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        screen.blit(self.player.image, self.player.rect)

        # actions passives des plateformes
        for platform in self.all_platforms:
            screen.blit(self.platform.image, self.platform.rect)

        # recuperer les fleches du joueur
        for arrow in self.player.all_arrow:
            arrow.move()

        #pdate joueur
        self.player.attraction()
        #self.player.check_shooting()
        self.player.update_health_bar(screen)
        self.player.update_animation()

        #update monstres
        for monster in self.all_monsters:
            monster.attraction()
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        # appliquer les images
        self.player.all_arrow.draw(screen)
        self.all_monsters.draw(screen)

        # Actions joueur
        for monster in self.all_monsters:
            monster.velocity = monster.normal_speed #sinon il mémorise la dernière vitesse trop élevée
        for arrow in self.player.all_arrow:
            arrow.velocity = arrow.normal_velocity

        if self.pressed.get(pygame.K_RIGHT) and self.player.canMove and not self.pressed.get(pygame.K_LEFT):
            if self.player.rect.x <= 300:
                self.player.move_right()
            if self.player.rect.x > 300:
                if self.background.rect.x <= - self.background.length + c.SCREEN_WIDTH + 10: #si on est au bout de la map
                    self.player.move_right()
                else:
                    self.background.move_left(self.player)
                    if not self.player.midair:
                        self.player.images = self.player.animations.get('move_R')
                        f.next_image(self.player, self.player.animations.get('move_R'))
                    self.background.move_left2(self.player)
                    for monster in self.all_monsters:
                        monster.velocity = monster.left_speed
                    for arrow in self.player.all_arrow:
                        arrow.velocity = arrow.right_velocity

        if self.pressed.get(pygame.K_LEFT) and self.player.canMove and not self.pressed.get(pygame.K_RIGHT):
            if self.player.rect.x >= 100:
                self.player.move_left()
            if self.player.rect.x < 100:
                if self.background.rect.x >= 0:
                    self.player.move_left()
                else:
                    self.background.move_right(self.player)
                    if not self.player.midair:
                        self.player.images = self.player.animations.get('move_L')
                        f.next_image(self.player, self.player.animations.get('move_L'))
                    self.background.move_right2(self.player)
                    for monster in self.all_monsters:
                        monster.velocity = monster.right_speed
                    for arrow in self.player.all_arrow:
                        arrow.velocity = arrow.left_velocity

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)