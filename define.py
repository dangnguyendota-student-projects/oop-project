from setting import *
from pygame import *

class Define:
    def __init__(self,map):
        self.map = map
        self.truoc = []
        for x in range(WIDTH):
            for y in range(HEIGHT):
                self.truoc.append(-1)



    def ke(self, s):
        T = []
        v = [s%WIDTH, s//WIDTH]
        if v[1] >= 1 and self.map[v[1]-1][v[0]] == 1:
            T.append(v[0] + (v[1]-1)*WIDTH)
        if v[1] <= HEIGHT-2 and self.map[v[1]+1][v[0]] == 1:
            T.append(v[0] + (v[1]+1)*WIDTH)
        if v[0] >= 1 and self.map[v[1]][v[0]-1] == 1:
            T.append(v[0]-1 + v[1]*WIDTH)
        if v[0] <= WIDTH-2 and self.map[v[1]][v[0]+1] == 1:
            T.append(v[0]+1 + v[1]*WIDTH)
        return T

    def search(self, s, xet):
        if xet[s] == False:
            self.truoc[s] = s
        temp = self.ke(s)
        for i in temp:
            if xet[i] == False :
                if (self.map[s//WIDTH][s%WIDTH] == 1 or self.map[s//WIDTH][s%WIDTH] == 6) or\
                (self.map[s // WIDTH][s % WIDTH] == 2 and s-i == WIDTH) or\
                (self.map[s // WIDTH][s % WIDTH] == 3 and i-s == 1) or\
                (self.map[s // WIDTH][s % WIDTH] == 4 and i-s ==WIDTH) or\
                (self.map[s // WIDTH][s % WIDTH] == 5 and s-i == 1):
                    self.truoc[i] = s
                    xet[i] = True
                    self.search(i,xet)
    def get(self):
        xet = []
        huong = []
        for x in range(WIDTH):
            for y in range(HEIGHT):
                xet.append(False)
                huong.append(-1)
        for x in range(WIDTH):
            for y in range(HEIGHT):
                if 2<= self.map[y][x] <= 6:
                    self.search(x + y * WIDTH,xet)
        for i in range(len(self.truoc)):
            if self.truoc[i] == -1 and self.map[i // WIDTH][i % WIDTH] == 0:
                huong[i] = 'nothing'
            elif self.truoc[i] == -1 and 1 <= self.map[i // WIDTH][i % WIDTH] <= 5 and self.ke(i)!=[]:
                if self.map[i // WIDTH][i % WIDTH] == 1  and (self.ke(i)[0] - i) % WIDTH == 0 or \
                (self.map[i // WIDTH][i % WIDTH] == 2 or self.map[i // WIDTH][i % WIDTH] == 4):
                    huong[i] = 'doc'
                else:
                    huong[i] = 'ngang'
            elif self.truoc[i] - i == 1:
                huong[i] = 'phai'
            elif self.truoc[i] - i == -1:
                huong[i] = 'trai'
            elif self.truoc[i] - i == WIDTH:
                huong[i] = 'len'
            elif self.truoc[i] - i == -WIDTH:
                huong[i] = 'xuong'
        return huong





