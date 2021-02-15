import pygame
import math
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720))
from game import Game
import constants as c


# Chargements des différents composants et paramètres

# background = pygame.image.load('assets/quiberon.jpg')
banner = pygame.image.load('assets/monster.png')
# banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)
play_button = pygame.image.load('assets/platform.png')
play_button_rect = play_button.get_rect()
play_button_rect.x = 150
play_button_rect.y = 250
game = Game('LVL/lvl_1', 'LVL/lvl_1_fond')
pygame.display.set_caption("Arrow Legend")
# icon = pygame.image.load('.png')
# pygame.display.set_icon(icon)


running = True
while running:
    screen.fill((200, 200, 200))
    if game.is_playing:
        game.player.in_menu = False
        #screen.blit(game.background.image2, (game.background.rect2.x, game.background.rect2.y))
        screen.blit(game.background.image, (game.background.rect.x, game.background.rect.y))
        game.update(screen)
    else:
        screen.blit(banner, (0,0))
        screen.blit(play_button, play_button_rect)
        game.player.check_menu()
        screen.blit(game.player.image, (game.player.rect.x + 200, -300))

    # mettre à jour l'ecran
    clock.tick(60)
    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            #Actions simples
            if event.key == pygame.K_UP and game.player.midair:
                game.player.double_jump()
            if event.key == pygame.K_UP and not game.player.midair:
                game.player.jump()
            if event.key == pygame.K_SPACE and not game.player.midair:
                game.player.canJump = False
                game.player.canMove = False #Sinon le joueur peut sauter et bouger pendant le chargement de l'arc
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            if event.key == pygame.K_SPACE:
                game.player.shoot()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()


