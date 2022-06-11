from setting import *
from math import inf


class a_search():
    def __init__(self, M):
        self.map = M

    @staticmethod
    def dist_between(x, y):
        if x//WIDTH == y//WIDTH or x%WIDTH == y%WIDTH:
            return 1
        else:
            return inf

    def ke(self, s):
        T = []
        v = [s%WIDTH, s//WIDTH]
        if v[1] >= 1 and 1 <= self.map[v[1]-1][v[0]] <= 6:
            T.append(v[0] + (v[1]-1)*WIDTH)
        if v[1] <= HEIGHT-2 and 1 <= self.map[v[1]+1][v[0]] <= 6:
            T.append(v[0] + (v[1]+1)*WIDTH)
        if v[0] >= 1 and 1 <= self.map[v[1]][v[0]-1] <= 6:
            T.append(v[0]-1 + v[1]*WIDTH)
        if v[0] <= WIDTH and 1 <= self.map[v[1]][v[0]+1] <= 6:
            T.append(v[0]+1 + v[1]*WIDTH)
        return T

    @staticmethod
    def lowest(a, b):
        temp = a[0]
        for i in a:
            if b[i] < b[temp]:
                temp = i
        return temp

    @staticmethod
    def reconstruct_path(cameFrom, current):
        total_path = [current]
        while 0 <= current < len(cameFrom):
            current = cameFrom[current]
            total_path.append(current)
        total_path.remove(current)
        total_path1 = []
        for i in range(len(total_path)):
            total_path1.append(total_path[len(total_path) - 1 - i])
        return total_path1

    @staticmethod
    def heuristic_cost_estimate(start, goal):
        return ((start % WIDTH - goal % WIDTH) ** 2 + (start // WIDTH - goal // WIDTH) ** 2) ** (1 / 2)

    def A(self, start, goal):
        closedSet = []
        openSet = [start]
        cameFrom = []
        gScore = []
        fScore = []
        for i in range(len(self.map) * len(self.map[0])):
            cameFrom.append(-1)
            gScore.append(inf)
            fScore.append(inf)
        gScore[start] = 0
        fScore[start] = self.heuristic_cost_estimate(start, goal)
        while openSet != []:
            current = self.lowest(openSet, fScore)
            if current == goal:
                return self.reconstruct_path(cameFrom, current)
            openSet.remove(current)
            closedSet.append(current)
            for neighbor in self.ke(current):
                if neighbor in closedSet:
                    continue
                if neighbor not in openSet:
                    openSet.append(neighbor)
                tentative_gScore = gScore[current] + self.dist_between(current, neighbor)
                if tentative_gScore >= gScore[neighbor]:
                    continue
                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = gScore[neighbor] + self.heuristic_cost_estimate(neighbor, goal)
        return False
