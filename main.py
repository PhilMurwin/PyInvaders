from re import X
import pygame, sys
from game import Game
from crt import CRT

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('PyInvaders')
    game_icon = pygame.image.load('graphics/red.png')
    pygame.display.set_icon(game_icon)
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width,screen_height))
    clock = pygame.time.Clock()
    game = Game(screen)
    crt = CRT(screen)

    ALIENLASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIENLASER,800)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == ALIENLASER:
                game.alien_shoot()

        screen.fill((30,30,30))
        game.run()
        crt.draw()

        pygame.display.flip()
        clock.tick(60)