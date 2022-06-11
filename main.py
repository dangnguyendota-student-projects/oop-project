from sprites import *
from define import *
from datetime import datetime
from math import fabs


def minmax(x, y):
    if x <= y:
        return [x, y]
    else:
        return [y, x]

class Game():
    def __init__(self):
        init()
        mixer.init()
        self.clock = time.Clock()
        display.set_caption(TITLE)
        mouse.set_visible(False)
        self.time = time.get_ticks()
        self.music = True
        self.v = 1

    def new(self, map, gameType, level_campain):

        self.screen = display.set_mode((DISWIDTH, DISHEIGHT))
        self.maxScoreCampaign = 1
        self.level = 8000
        self.score = 0
        self.running = True
        self.level_campaign = level_campain
        self.sprites = sprite.Group()
        self.mouses = sprite.Group()
        self.doors = sprite.Group()
        self.foods = sprite.Group()
        self.monsters = sprite.Group()
        self.buttons = sprite.Group()
        self.diem = sprite.Group()
        self.effect = sprite.Group()
        self.map = map
        self.gameType= gameType
        self.mouses.add(Mouse(self))
        self.search = Define(self.map)
        self.huong = self.search.get()
        for x in range(WIDTH):
            for y in range(HEIGHT):
                if self.map[y][x] == 6:
                    self.door = Door(self, x, y)
                    self.doors.add(self.door)
                    self.x = x
                    self.y = y
                if 1 <= self.map[y][x] <= 5:
                    self.sprites.add(Conveyor(self, x, y))
                if 7 <= self.map[y][x] <= 10:
                    self.monsters.add(Monster(self, x, y, self.map[y][x]))
        temp = []
        for i in self.monsters:
            if i.need not in temp:
                temp.append(i.need)
        temp.append(len(food) - 1)
        t = randrange(0, len(temp))
        self.foods.add(Food(self, self.x, self.y, temp[t], self.v))
        self.newButton()
        self.getMap()
        self.flag_effect = False

    def run(self):
        music.play(-1)
        while self.running:
            if self.music:
                music.set_volume(1)
            else:
                music.set_volume(0)
            self.event()
            self.update()
            self.draw()
            self.complete()
            self.clock.tick(FPS)
            display.update()

    def event(self):
        for e in event.get():
            if e.type == QUIT:
                quit()
                exit()
            if e.type == KEYDOWN:
                all_keys = key.get_pressed()
                if e.key == K_ESCAPE:
                    quit()
                    exit()
                if all_keys[K_s] and (all_keys[K_LCTRL] or all_keys[K_RCTRL]):
                    text = 'image/save/' + str(datetime.now()).split(':')[0] + '--' + \
                           str(datetime.now()).split(':')[1] + '--' + str(datetime.now()).split(':')[2] + '.png'
                    image.save(self.screen, text)
            if e.type == MOUSEBUTTONDOWN:
                if self.music:
                    click.play(0)
                m = VEC((VEC(mouse.get_pos()).x - VI_TRIX) // SIZE,
                        (VEC(mouse.get_pos()).y - VI_TRIY) // SIZE)
                if e.button == 1 and 0 <= m.x < WIDTH and 0 <= m.y < HEIGHT and self.getLenFriend(m.y, m.x) > 2:
                    if 2 <= self.map[int(m.y)][int(m.x)] <= 4:
                        self.map[int(m.y)][int(m.x)] += 1
                    elif self.map[int(m.y)][int(m.x)] == 5:
                        self.map[int(m.y)][int(m.x)] = 2
                    self.search.map = self.map
                    self.huong = self.search.get()
                    for i in self.sprites:
                        i.kill()
                    for x in range(WIDTH):
                        for y in range(HEIGHT):
                            if 1 <= self.map[y][x] <= 5:
                                self.sprites.add(Conveyor(self, x, y))
                if e.button == 1:
                    if 1260 <= mouse.get_pos()[0] <= 1305 and 0 <= mouse.get_pos()[1] <= 45:
                        self.running = False
                        music.set_volume(0)

    def update(self):
        self.sprites.update()
        self.mouses.update()
        self.doors.update()
        self.foods.update()
        self.monsters.update()
        self.buttons.update()
        self.diem.update()
        self.effect.update()
        self.edit()
        if time.get_ticks() - self.time > self.level and not self.flag_effect:
            self.time = time.get_ticks()
            temp = []
            for i in self.monsters:
                if i.need not in temp:
                    temp.append(i.need)
            temp.append(len(food) - 1)
            t = randrange(0, len(temp))
            self.foods.add(Food(self, self.x, self.y, temp[t], self.v))

    def draw(self):
        self.screen.blit(background, (0, 0))
        self.drawEnvironment()
        self.sprites.draw(self.screen)
        self.drawMap()
        self.foods.draw(self.screen)
        self.monsters.draw(self.screen)
        self.doors.draw(self.screen)
        self.buttons.draw(self.screen)
        self.diem.draw(self.screen)
        self.effect.draw(self.screen)
        self.mouses.draw(self.screen)
        m = VEC((VEC(mouse.get_pos()).x - VI_TRIX) // SIZE,
                (VEC(mouse.get_pos()).y - VI_TRIY) // SIZE)
        display.set_caption(str(m.x + m.y * WIDTH) + ':' + str(m))

    def drawMap(self):
        m = VEC((VEC(mouse.get_pos()).x - VI_TRIX) // SIZE,
                (VEC(mouse.get_pos()).y - VI_TRIY) // SIZE)
        for i in range(WIDTH):
            for j in range(HEIGHT):
                if 2 <= self.map[j][i] <= 5:
                    if m.x == i and m.y == j and self.getLenFriend(j, i) > 2:
                        self.screen.blit(button_click[self.map[j][i] - 2],
                                         (i * SIZE + VI_TRIX, j * SIZE + VI_TRIY))
                    else:
                        if self.getLenFriend(j, i) > 2:
                            self.screen.blit(button[self.map[j][i] - 2],
                                             (i * SIZE + VI_TRIX, j * SIZE + VI_TRIY))

        self.screen.blit(score, (600, 5))
        text = FONT1.render(': ' + str(self.score), True, Color("black"), None)
        self.screen.blit(text, (700, 10))
        for i in self.monsters:
            self.screen.blit(dream[i.need], (i.rect.x, i.rect.y - SIZE))

    def drawEnvironment(self):
        for x in range(WIDTH):
            for y in range(HEIGHT):
                if self.map[y][x] == 11:
                    self.screen.blit(flower, (x*SIZE + VI_TRIX, y*SIZE + VI_TRIY))
                elif self.map[y][x] == 12:
                    self.screen.blit(box2, (x*SIZE + VI_TRIX, y*SIZE + VI_TRIY))
                elif self.map[y][x] == 13:
                    self.screen.blit(box1, (x*SIZE + VI_TRIX, y*SIZE + VI_TRIY))
                elif self.map[y][x] == 14:
                    self.screen.blit(cart1, (x*SIZE + VI_TRIX, y*SIZE + VI_TRIY))

    def edit(self):
        for i in range(WIDTH):
            for j in range(HEIGHT):
                if self.map[j][i] == 2:
                    if j == 0 or (j > 0 and (self.map[j - 1][i] > 5 or self.map[j - 1][i] == 0)):
                        self.map[j][i] = 3
                if self.map[j][i] == 3:
                    if i == WIDTH - 1 or (i < WIDTH - 1 and (self.map[j][i + 1] > 5 or self.map[j][i + 1] == 0)):
                        self.map[j][i] = 4
                if self.map[j][i] == 4:
                    if j == HEIGHT - 1 or (j < HEIGHT - 1 and (self.map[j + 1][i] > 5 or self.map[j + 1][i] == 0)):
                        self.map[j][i] = 5
                if self.map[j][i] == 5:
                    if i == 0 or (i > 0 and (self.map[j][i - 1] > 5 or self.map[j][i - 1] == 0)):
                        self.map[j][i] = 2

    def getMap(self):
        for x in range(HEIGHT):
            for y in range(WIDTH):
                if self.map[x][y] in [2, 3, 4, 5]:
                    print(x,',',y,',',self.getLenFriend(x, y))
                    if self.getLenFriend(x, y) == 2:
                        pass

    def getLenFriend(self, x, y):
        return len(self.getFriend(x, y))

    def getFriend(self, x, y):
        a = [-1, 0, 1]
        b = [-1, 0, 1]
        if 0 < x < HEIGHT - 1 :
            if y == 0:
                b = [0, 1]
            elif y == WIDTH - 1:
                b = [-1, 0]
        elif 0 < y < WIDTH - 1:
            if x == 0:
                a = [0, 1]
            elif x == HEIGHT:
                a = [-1, 0]
        elif x == 0 and y == 0:
            a = [0, 1]
            b = [0, 1]
        elif x == 0 and y == WIDTH:
            a = [0, 1]
            b = [-1, 0]
        elif x == HEIGHT and y == 0:
            a = [-1, 0]
            b = [0, 1]
        elif x == HEIGHT and y == WIDTH:
            a = [-1, 0]
            b = [-1, 0]
        friend = []
        for i in a:
            for j in b:
                if fabs(i) + fabs(j) == 1:
                    if self.map[int(x) + i][int(y) + j] in [1, 2, 3, 4, 5, 6]:
                        friend.append([int(x)+i, int(y)+j])
        return friend

    def getWayCanMove(self):
        pass

    def isOpp(self, x, y):
        if 2 <= self.map[y][x] <= 5:
            for i in range(WIDTH):
                for j in range(HEIGHT):
                    if j != y and i == x and \
                            (self.map[y][x] == 2 and self.map[j][i] == 4 and y > j) or \
                            (self.map[y][x] == 4 and self.map[j][i] == 2 and y < j):
                        temp = 0
                        for t in range(minmax(y, j)[0], minmax(y, j)[1]):
                            if self.map[t][x] != 1 and t != y and t != j:
                                temp = 0
                                break
                            else:
                                temp += 1
                        if temp == abs(y - j):
                            return True
                    elif i != x and j == y and \
                            (self.map[y][x] == 3 and self.map[j][i] == 5 and x < i) or \
                            (self.map[y][x] == 5 and self.map[j][i] == 3 and x > i):
                        temp = 0
                        for t in range(minmax(x, i)[0], minmax(x, i)[1]):
                            if self.map[y][t] != 1 and t != x and t != i:
                                temp = 0
                                break
                            else:
                                temp += 1
                        if temp == abs(x - i):
                            return True
        return False

    def blit(self, x, y):
        self.screen.blit(x, y)

    def mouseEvent(self):
        pass

    def newButton(self):
        self.buttons.add(Button(self, 1260, 0, 4))
        #self.buttons.add(Button(self, 800, 0, 5))

    def levelUp(self):
        if self.v == 3:
            self.v = 1
        else:
            self.v += 1
        print(self.v)

    def complete(self):
        if self.gameType == 'campaign' and self.score >= self.maxScoreCampaign and self.level_campaign < 5 and not self.flag_effect:
            self.effect.add(winGame(self))
            for i in self.foods:
                i.kill()
            self.flag_effect = True

    def quaMan(self):
        self.running = False
        map_campaign = []
        with open('map/level{}.txt'.format(self.level_campaign + 1), 'r') as lines:
            for line in lines:
                temp = []
                for j in line:
                    try:
                        temp.append(int(j))
                    except:
                        if j == '-':
                            temp.append(int(10))
                        elif j == 'f':
                            temp.append((int(11)))
                        elif j == 'a':
                            temp.append((int(12)))
                        elif j == 'b':
                            temp.append((int(13)))
                        elif j == 'c':
                            temp.append((int(14)))

                map_campaign.append(temp)
        self.new(map_campaign, 'campaign', self.level_campaign + 1)
        self.run()
