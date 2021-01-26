import pygame 
import queue 
from Grid import Grid

pygame.init

class Algorithm:

    def __init__(self, screen, colour):
        self.screen = screen
        self.colour = colour
        self.blockSize = 100

    def maze(self):
        maze = []
        maze.append(["O", " ", " ", " " , " "])
        maze.append(["#", "#", "#", "#" , " "])
        maze.append([" ", " ", " ", " " , " "])
        maze.append([" ", "#", " ", "#" , "#"])
        maze.append([" ", "#", " ", " " , "X"])

        return maze

    def validMove(self, maze, path):
        for i, currentPosition in enumerate(maze[0]):
            if currentPosition == "O":
                start = i
        
        x = start
        y = 0

        for move in path:
            if move == "L":
                y -= 1
            
            if move == "R":
                y += 1

            if move == "U":
                x -= 1

            if move == "D":
                x += 1

            if not(0 <= x < len(maze[0]) and 0 <= y < len(maze)):
                return False
            elif (maze[x][y] == "#"):
                return False
        
        return True
    
    def checkIfEnd(self, maze, path):
        for i, currentPosition in enumerate(maze[0]):
            if currentPosition == "O":
                start = i
        
        x = start
        y = 0

        for move in path:
            if move == "L":
                y -= 1
            
            if move == "R":
                y += 1
            
            if move == "U":
                x -= 1
            
            if move == "D":
                x += 1
            
        if maze[x][y] == "X":
            self.drawSolution(path)
            return True

        return False
    
    def breadthFirstSearch(self):
        path = queue.Queue()
        path.put("")
        add = ""

        maze = self.maze()

        while not self.checkIfEnd(maze, add):
            add = path.get()
            
            for i in ("D", "U", "L", "R"):
                move = add + i
                if self.validMove(maze, move):
                    path.put(move)
    
    def drawSolution(self, path):
        x = 10
        y = 10

        for move in path:
            if move == "L":
                y = y - self.blockSize
                pygame.draw.rect(self.screen, self.colour, [y, x, self.blockSize, self.blockSize])
            
            if move == "R":
                y = y + self.blockSize
                pygame.draw.rect(self.screen, self.colour, [y, x, self.blockSize, self.blockSize])
            
            if move == "U":
                x = x - self.blockSize
                pygame.draw.rect(self.screen, self.colour, [y, x, self.blockSize, self.blockSize])
            
            if move == "D":
                x = x + self.blockSize
                pygame.draw.rect(self.screen, self.colour, [y, x, self.blockSize, self.blockSize])