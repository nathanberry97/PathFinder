import pygame
pygame.init

def main():
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    white = (255, 255, 255)

    size = x, y = 520, 520
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Path Finder')

    gameMenu = True

    while gameMenu:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameMenu = False
        
        screen.fill(black)
      
        grid(screen, white)

        pygame.display.update()
            
    pygame.quit

def grid(screen, colour):
    dx = 10
    dy = 10

    for x in range(0, 5):
        for y in range (0, 5):
            pygame.draw.rect(screen, colour,[dx, dy, 100, 100], 2)
            dy = dy + 100
        dx = dx + 100
        dy = 10
    dx = 10

main()