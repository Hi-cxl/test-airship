import sys
import pygame
from rain import Rain
from pygame.sprite import Group

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1000,600))

    bg_color = (230,230,230)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(bg_color)
        pygame.display.flip()


run_game()