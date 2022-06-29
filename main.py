import pygame
import math
from queue import PriorityQueue
from node import Node

pygame.init

# vars
WIDTH = 600
HEIGHT = 600
# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

# Objects
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Path-finder Algorithm")


# main-loop
def main(win, width, height):
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        win.fill(WHITE)
        pygame.display.update()


def draw_grid():
    pass


main(SCREEN, WIDTH, HEIGHT)
