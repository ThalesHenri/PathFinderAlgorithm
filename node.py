import pygame

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

pygame.init()


class Node:
    def __init__(self, rows, col, width, total_rows):
        self.rows = rows
        self.col = col
        self.x = rows * width
        self.y = col * width
        self.color = WHITE
        self.neighbor = []
        self.width = width
        self.total_rows = total_rows

    """This functions will represent the states of the nodes in the grid
    and return his collors"""

    def get_pos(self):
        return self.rows, self.col

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_obstacle(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == PURPLE

    def reset(self):
        self.color == WHITE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_obstacle(self):
        self.color = BLACK

    def make_start(self):
        self.color = ORANGE

    def make_end(self):
        self.color = PURPLE

    def make_path(self):
        self.color = TURQUOISE

    def draw(self, win):
        pygame.draw.rect(win, self.color,(self.x, self.y, self.width, self.width))

    def update_neighbors(self):
        pass

    def __lt__(self, other):
        return False
