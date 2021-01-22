import pygame 
pygame.init

class Grid:

    gridX = 10
    gridY = 10
    gridSize = 20

    startNode = 10
    endNode = 490

    def __init__(self, screen):
        self.screen = screen

    def grid(self, colour):
        for x in range (0, 25):
            for y in range (0, 25):
                pygame.draw.rect(self.screen, colour, [self.gridX, self.gridY, self.gridSize, self.gridSize], 1)
                self.gridY = self.gridY + self.gridSize
            self.gridX = self.gridX + self.gridSize
            self.gridY = 10
        self.gridX = 10

    def node(self, startColour, endColour):
        pygame.draw.rect(self.screen, startColour,[self.startNode, self.startNode, self.gridSize, self.gridSize])
        pygame.draw.rect(self.screen, endColour,[self.endNode, self.endNode, self.gridSize, self.gridSize])

    def wall(self, colour):
        wallOneX = 90
        wallOneY = 290

        wallTwoX = 230
        wallTwoY = 70

        wallThreeX = 370
        wallThreeY = 430

        for x in range(0, 7):
            pygame.draw.rect(self.screen, colour, [wallOneX, wallOneY, self.gridSize, self.gridSize])
            wallOneX = wallOneX + self.gridSize
            pygame.draw.rect(self.screen, colour, [wallThreeX, wallThreeY, self.gridSize, self.gridSize])
            wallThreeX = wallThreeX + self.gridSize
        
        for y in range(0, 12):
            pygame.draw.rect(self.screen, colour, [wallTwoX, wallTwoY, self.gridSize, self.gridSize])
            wallTwoY = wallTwoY + self.gridSize
