import pygame
import time

pygame.init()# initiates the pygame

# window config
gwindow = pygame.display.set_mode((720, 720))
pygame.display.set_caption("born to earth")


# helpful variables
exit_flag = False
game_over = False

# creating loops

while not exit_flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_flag = True

pygame.quit()