import pygame 
pygame.init

class Grid:

    def __init__(self, screen):
        self.screen = screen
        self.gridX = 10
        self.gridY = 10
        self.gridSize = 100

    def grid(self, colour):
        for x in range (0, 5):
            for y in range (0, 5):
                pygame.draw.rect(self.screen, colour, [self.gridX, self.gridY, self.gridSize, self.gridSize], 1)
                self.gridY = self.gridY + self.gridSize
            self.gridX = self.gridX + self.gridSize
            self.gridY = 10
        self.gridX = 10

    def node(self, startColour, endColour):
        startNode = 10
        endNode = 410

        pygame.draw.rect(self.screen, startColour,[startNode, startNode, self.gridSize, self.gridSize])
        pygame.draw.rect(self.screen, endColour,[endNode, endNode, self.gridSize, self.gridSize])

    def wall(self, colour):
        wallOneX = 10
        wallOneY = 110

        wallTwoX = 110
        wallTwoY = 310

        wallThreeX = 310
        wallThreeY = 310

        for x in range(0, 4):
            pygame.draw.rect(self.screen, colour, [wallOneX, wallOneY, self.gridSize, self.gridSize])
            wallOneX = wallOneX + self.gridSize
        
        for y in range(0, 2):
            pygame.draw.rect(self.screen, colour, [wallTwoX, wallTwoY, self.gridSize, self.gridSize])
            wallTwoY = wallTwoY + self.gridSize

            pygame.draw.rect(self.screen, colour, [wallThreeX, wallThreeY, self.gridSize, self.gridSize])
            wallThreeX = wallThreeX + self.gridSize