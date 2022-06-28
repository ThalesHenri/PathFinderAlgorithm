import pygame

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
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

# Object's
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

def main(win, width, height):
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        win.fill(WHITE)
        pygame.display.update()
        
main(SCREEN, WIDTH, HEIGHT)
