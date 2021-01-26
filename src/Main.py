from Grid import Grid
from Algorithm import Algorithm
import pygame
pygame.init

def main():
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    WHITE = (255, 255, 255)
    GREY = (128, 128, 128)

    size = x, y = 520, 520
    display = pygame.display.set_mode(size)
    pygame.display.set_caption('Path Finder')

    begin = True
   
    border = Grid(display)

    while begin:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                begin = False
        
        display.fill(WHITE)

        border.node(GREEN, RED)
        border.wall(GREY)
        border.grid(BLACK)

        pygame.display.update()
    
    pygame.quit

main()