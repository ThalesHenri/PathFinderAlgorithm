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
