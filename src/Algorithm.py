import pygame 
pygame.init

class Algorithm:

    numRows = 25
    numCol = 25

    costToVist =[[]] # ToDo set all cost to infinity then update to a cost of 1 once it can be reached from current node 
    checkIfVisited =[[]] # set all nodes to 0 and update to 1 once visted 
    shortestPath = [] # store the path values and print out the shortest path once found from 

    def arrayBulider (self):
        self.costToVist = [[0 for i in range(self.numCol)]for j in range(self.numRows)] 
        self.checkIfVisited = [[0 for i in range(self.numCol)]for j in range(self.numRows)] 

        self.checkIfVisited[0][0] = 1

        for x in range(0, 25):
            for y in range(0, 25): 
                self.costToVist[0][0] = 0
                self.costToVist[x][y] = float('inf')   

        print(self.costToVist)
        print(self.checkIfVisited) 
    

    def dijkstra(self, screen, colour):

        while self.visited[24][24] == 0:
            pass
        # need to implement algorithm to update grid till visted[24][24] = 1, then return shortest path