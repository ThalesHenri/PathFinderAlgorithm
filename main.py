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
    ROWS = 50  # changing that will make the board to have more or less squares
    grid = make_grid(ROWS, width)

    start = None
    end = None

    run = True
    started = False

    while run:
        draw(SCREEN, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if started:
                continue

            if pygame.mouse.get_pressed()[0]:  # Left mouse button
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                if not start:
                    start = node
                    start.make_start()  # will change the color of the node

                elif not end:
                    end = node
                    node.make_end()

                elif node != start and node != end:
                    node.make_obstacle()  # will make a node a obstacle

            elif pygame.mouse.get_pressed()[2]:  # right
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                elif node == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:  # will start the algorithm
                    pass

    pygame.quit()


def draw_grid(win, rows, width):  # will draw the grid's lines
    gap = width // int(rows)
    for a in range(rows):
        pygame.draw.line(win, GREY, (0, a * gap), (width, a * gap))
        for b in range(rows):
            pygame.draw.line(win, GREY, (a * gap, 0), (a * gap, width))


# the main responsable for draw in the grid, will call other functions
def draw(win, grid, rows, width):
    win.fill(WHITE)

    for row in grid:
        for node in row:
            node.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos
    row = y // gap
    col = x // gap
    return row, col


# will uses manhantan distance formula, kinda a L distance
def heuristic(p1, p2):
    x1, x2 = p1
    y1, y2 = p2
    return abs(x1 - x2) + abs(y1, y2)


# the main algorithm funciton
def pathfinder():
    pass


""" will create a 2d list like that [[],[],[],[]] and in every position of
that list will have a node object"""


def make_grid(rows, width):

    grid = []
    gap = width // rows
    for a in range(rows):
        grid.append([])
        for b in range(rows):
            node = Node(a, b, gap, rows)
            grid[a].append(node)

    return grid


main(SCREEN, WIDTH, HEIGHT)
