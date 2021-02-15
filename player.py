import pygame
import constants as c
import functions as f
from arrow_left import ArrowLeft
from arrow_right import ArrowRight
import animation


class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__('player')
        self.game = game
        #Specs
        self.health = 100
        self.max_health = 100
        self.attack = 25
        self.y_vel = 0
        self.velocity = 8
        #Inventory
        self.all_arrow = pygame.sprite.Group()
        #Images
        self.menu_images = f.load_list('assets/menu_pos')
        #self.shot_left_images = f.load_list('assets/Images/Shooting_left_150x150')
        #self.shot_right_images = f.load_list('assets/Images/Shooting_right_150x150')
        #self.moving_left_images = f.load_list('assets/Images/Move_left_150x150')
        #self.moving_right_images = f.load_list('assets/Images/Move_right_150x150')
        #self.jump_left_image = f.load_image('assets/Images/Jump_left_150x150/Jump_left_00.png')
        #self.jump_right_image = f.load_image('assets/Images/Jump_right_150x150/Jump_right_00.png')
        #self.double_jump_left_images = f.load_list('assets/Images/Double_jump_left_150x150')
        #self.double_jump_right_images = f.load_list('assets/Images/Double_jump_right_150x150')
        #self.current_nb = 0
        #self.static_left_image = f.load_image('assets/Images/Static_left_150x150/Static_left_00.png')
        #self.static_right_image = f.load_image('assets/Images/Static_right_150x150/Static_right_00.png')
        #self.image = self.moving_right_images[self.current_nb]
        #States
        self.in_menu = True
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.ground = c.GROUND_HEIGHT - self.image.get_height() + 50
        self.rect.y = self.ground
        self.midair = False
        self.acc = 0
        self.gravity = c.GRAVITY
        self.orientation = 1 #1 means risght, 0 means left
        self.has_doubleJumped = False

    def update_animation(self):
        self.animate()

    def attraction(self):
        if self.midair:
            self.acc += self.gravity
            if self.y_vel < c.MAX_Y_VEL:
                self.y_vel += self.acc
            self.rect.y += self.y_vel
        if self.rect.y > self.ground:
            if self.orientation == 0:
                self.images = self.animations.get('static_L')
            else:
                self.images = self.animations.get('static_R')
            self.rect.y = self.ground
            self.acc = 0
            self.y_vel = 0
            self.gravity = c.GRAVITY
            self.midair = False
            self.has_doubleJumped = False
        #if self.center_x in []

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, c.GRAY, [self.rect.x + 100, self.rect.y + 40, self.max_health, 7])
        pygame.draw.rect(surface, c.CYAN, [self.rect.x + 100, self.rect.y + 40, self.health, 7])

    def shoot(self):
        if self.canShoot and not self.midair:
            if self.orientation == 1:
                self.start_animation('shoot_R', allow_jump=False, allow_shoot=False, allow_move=False)
                self.all_arrow.add(ArrowRight(self))
            else:
                self.start_animation('shoot_L', allow_jump=False, allow_shoot=False, allow_move=False)
                self.all_arrow.add(ArrowLeft(self))

    def check_menu(self):
        if self.in_menu or not self.game.is_playing:
            f.next_image(self, self.menu_images)

    #def check_shooting(self):
     #   if self.is_shooting and self.orientation == 1:
      #      f.next_image(self, self.shot_right_images)
       # if self.is_shooting and self.orientation == 0:
        #    f.next_image(self, self.shot_left_images)

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.orientation = 1
            self.rect.x += self.velocity
            if self.midair and not self.doubleJumping:      #on ne modifie l'image que si le double_jump est fini (car canMove est actif)
                self.images = self.animations.get('jump_R')
            if not self.midair:  # à terre
                self.images = self.animations.get('move_R')
                f.next_image(self, self.images)

    def move_left(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.orientation = 0
            self.rect.x -= self.velocity
            if self.midair and not self.doubleJumping:
                self.images = self.animations.get('jump_L')
            if not self.midair: #à terre
                self.images = self.animations.get('move_L')
                f.next_image(self, self.images)

    def jump(self):
        if self.canJump and not self.midair:
            self.midair = True
            self.doubleJumping = False
            self.y_vel += c.JUMP_VEL
            self.acc += c.JUMP_ACC
            if self.orientation == 0:
                self.start_animation('jump_L', allow_jump=False, allow_shoot=False)
            else:
                self.start_animation('jump_R', allow_jump=False, allow_shoot=False)

    def double_jump(self):
        if self.midair and not self.has_doubleJumped:
            self.doubleJumping = True
            self.has_doubleJumped = True
            self.acc = 0
            self.y_vel = 0
            self.y_vel += c.JUMP_VEL
            self.acc += c.JUMP_ACC
            # self.rotate(180)
            if self.orientation == 0:
                self.start_animation('doubleJump_L', allow_jump=False, allow_shoot=False)
            else:
                self.start_animation('doubleJump_R', allow_jump=False, allow_shoot=False)

    def rotate(self, angle):
        self.image = pygame.transform.rotozoom(self.image, angle, 1)

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.game_over()





