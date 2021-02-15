import pygame
import functions as f

#Création du dictionnaire qui va regrouper les images chargées par type de sprites
animations = {
    'spider': {
        'init': f.load_list('assets/Images/Monsters/Spider'), #à modifier par la suite
        'loop': f.load_list('assets/Images/Monsters/Spider')
    },
    'player': {
        'init': f.load_list('assets/Images/Players/Black_150x150/Static_R'), #à modifier par la suite
        'move_L': f.load_list('assets/Images/Players/Black_150x150/Move_L'),
        'move_R': f.load_list('assets/Images/Players/Black_150x150/Move_R'),
        'jump_L': f.load_list('assets/Images/Players/Black_150x150/Jump_L'),
        'jump_R': f.load_list('assets/Images/Players/Black_150x150/Jump_R'),
        'doubleJump_L': f.load_list('assets/Images/Players/Black_150x150/DoubleJump_L'),
        'doubleJump_R': f.load_list('assets/Images/Players/Black_150x150/DoubleJump_R'),
        'static_L': f.load_list('assets/Images/Players/Black_150x150/Static_L'),
        'static_R': f.load_list('assets/Images/Players/Black_150x150/Static_R'),
        'shoot_L': f.load_list('assets/Images/Players/Black_150x150/Shoot_L'),
        'shoot_R': f.load_list('assets/Images/Players/Black_150x150/Shoot_R')
    }
}


class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name):
        super().__init__()
        self.current_nb = 0
        self.animations = animations.get(sprite_name)
        self.images = self.animations.get('init')
        self.image = self.images[0]
        self.animated = False
        self.canJump = True
        self.canShoot = True
        self.canMove = True
        self.doubleJumping = False

    def start_animation(self, list_name, allow_jump=True, allow_shoot=True, allow_move=True):
        self.canJump = allow_jump
        self.canShoot = allow_shoot
        self.canMove = allow_move
        self.images = self.animations.get(list_name)
        self.image = self.images[0] #on commence à afficher la 1ere image ici et le reste dans animate()
        self.animated = True

    #definir une methode pour animer le sprite
    def animate(self, loop=False, busy=False):
        if self.animated:
            #passer à l'image suivante
            self.current_nb += 1
        if self.current_nb > len(self.images) - 1:
            self.current_nb = 0
            if loop is False:
                self.animated = False
                self.canJump = True
                self.canShoot = True
                self.canMove = True
                self.doubleJumping = False
        self.image = self.images[int(self.current_nb)]

