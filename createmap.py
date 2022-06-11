from setting import *
from define import *
from sprites import *


class createmap():
    def __init__(self):

        init()
        mixer.init()
        self.clock = time.Clock()
        display.set_caption(TITLE)
        mouse.set_visible(False)

    def newMap(self):
        self.screen = display.set_mode((DISWIDTH, DISHEIGHT))
        self.running = True
        self.saving = False
        self.ques = False
        self.mouses = sprite.Group()
        self.doors = sprite.Group()
        self.sprites = sprite.Group()
        self.monsters = sprite.Group()
        self.foods = sprite.Group()
        self.mouses.add(Mouse(self))
        self.map = []
        for y in range(HEIGHT):
            self.map.append([])
            for x in range(WIDTH):
                self.map[y].append(0)
        self.choose = 0
        self.choose_img = -1
        self.search = Define(self.map)
        self.huong = self.search.get()
        self.name = ''
        self.link = []
        with open('map/link.txt', 'r') as lines:
            for line in lines:
                self.link.append(line.split())

    def run(self):
        while self.running:
            self.event()
            self.update()
            self.draw()
            self.clock.tick(FPS)
            display.update()

    def event(self):
        for e in event.get():
            if e.type == QUIT:
                quit()
                exit()
            if e.type == KEYDOWN:
                if 97 <= e.key <= 122:
                    if len(self.name) <= 19:
                        self.name += chr(e.key)
                if e.key == 8:
                    self.name = self.name[:len(self.name) - 1]
                if e.key == K_RETURN:
                    if self.saving:
                        self.saving = False
                        text = ''
                        print(self.map)
                        for y in range(HEIGHT):
                            for x in range(WIDTH):
                                if self.map[y][x] < 10:
                                    text += str(self.map[y][x])
                                elif self.map[y][x] == 10:
                                    text+= '-'
                                elif self.map[y][x] == 11:
                                    text+= 'f'
                                elif self.map[y][x] == 12:
                                    text+= 'a'
                                elif self.map[y][x] == 13:
                                    text+= 'b'
                                elif self.map[y][x] == 14:
                                    text+= 'c'

                            text += '\n'
                        text1 = ''

                        for i in self.link:
                            text1 += i[0] + '\n'
                        text1 += 'map/' + self.name + '.txt\n'
                        f = open('map/' + self.name + '.txt', 'w')
                        f.write(text)
                        f.close()
                        f = open('map/link.txt', 'w')
                        f.write(text1)
                        f.close()
                        self.name = ""
                        self.running = False
                    elif self.ques:
                        self.ques = False
                if e.key == K_ESCAPE:
                    if self.saving:
                        self.saving = False
                    if self.ques:
                        self.ques = False


    def update(self):
        self.mouses.update()
        self.sprites.update()
        self.monsters.update()
        self.doors.update()
        self.foods.update()
        display.set_caption(str(mouse.get_pos()))

    def draw(self):
        self.screen.blit(background, (0, 0))
        self.drawGrid()
        self.drawEnvironment()
        self.drawSprites()
        self.sprites.draw(self.screen)
        self.monsters.draw(self.screen)
        self.doors.draw(self.screen)
        self.foods.draw(self.screen)
        self.drawMap()
        if not self.saving and not self.ques:
            self.mouseEvent()
        else:
            if self.saving:
                self.screen.blit(name, (300, 300))
                text1 = FONT1.render(self.name + '|', True, Color('black'), None)
                text2 = FONT1.render(self.name, True, Color('black'), None)
                if time.get_ticks() % 1000 < 500:
                    self.screen.blit(text1, (410, 310))
                else:
                    self.screen.blit(text2, (410, 310))
            elif self.ques:
                self.screen.blit(question, (900, 0))
        self.mouses.draw(self.screen)

    def drawGrid(self):
        for i in range(WIDTH + 1):
            draw.line(self.screen,
                      Color('green'),
                      (VI_TRIX + i * SIZE, VI_TRIY),
                      (VI_TRIX + i * SIZE, VI_TRIY + HEIGHT * SIZE), 2)
        for i in range(HEIGHT + 1):
            draw.line(self.screen,
                      Color('green'),
                      (VI_TRIX, VI_TRIY + i * SIZE),
                      (VI_TRIX + WIDTH * SIZE, VI_TRIY + i * SIZE), 2)
        draw.rect(self.screen, Color('black'), (1280, 100, SIZE, SIZE), 2)

    def drawSprites(self):
        m = mouse.get_pos()
        tap = []
        self.screen.blit(transform.scale(door_delay[0], (SIZE, SIZE)), (0, 0))
        tap.append(transform.scale(door_delay[0], (SIZE, SIZE)))
        for i in range(len(monster)):
            self.screen.blit(monster[i][0], (SIZE + i * SIZE, 0))
            tap.append(monster[i][0])
        for i in range(4):
            self.screen.blit(button[i], (SIZE + len(monster) * SIZE + i * SIZE, 0))
            tap.append(button[i])
        self.screen.blit(stop[0], (len(monster) * SIZE + 5 * SIZE, 0))
        tap.append(stop[0])
        draw.rect(self.screen, Color("green"), (len(monster) * SIZE + 10 * SIZE, 0, SIZE, SIZE), 2)
        self.screen.blit(flower, (len(monster) * SIZE + 6 * SIZE, 0))
        tap.append(flower)
        self.screen.blit(box2, (len(monster) * SIZE + 7 * SIZE, 0))
        tap.append(box2)
        self.screen.blit(box1, (len(monster) * SIZE + 8 * SIZE, 0))
        tap.append(box1)
        self.screen.blit(cart1, (len(monster) * SIZE + 9 * SIZE, 0))
        tap.append(cart1)

        if self.choose_img != -1 and self.choose_img < len(tap):
            self.screen.blit(tap[self.choose_img], (1280, 100))
        if self.choose_img == len(tap):
            draw.rect(self.screen, Color("green"), (1280, 100, SIZE, SIZE), 2)

        if 1240 <= m[0] <= 1340 and 10 <= m[1] <= 50:
            self.screen.blit(button_click[7], (1240, 10))
        else:
            self.screen.blit(button[7], (1240, 10))
        if 1100 <= m[0] <= 1200 and 10 <= m[1] <= 50:
            self.screen.blit(button_click[8], (1100, 10))
        else:
            self.screen.blit(button[8], (1100, 10))
        if 1200 <= m[0] <= 1240 and 10 <= m[1] <= 50:
            self.screen.blit(button_click[9], (1200, 10))
        else:
            self.screen.blit(button[9], (1200, 10))

    def mouseEvent(self):

        m = VEC((VEC(mouse.get_pos()).x - VI_TRIX) // SIZE,
                (VEC(mouse.get_pos()).y - VI_TRIY) // SIZE)

        mp = mouse.get_pos()
        tap = [6, 7, 8, 9, 10, 2, 3, 4, 5, 1, 11, 12, 13, 14, 0]

        if 0 <= m.x <= WIDTH - 1 and 0 <= m.y <= HEIGHT - 1:
            draw.rect(self.screen, Color('red'), (m.x * SIZE + VI_TRIX, m.y * SIZE + VI_TRIY, SIZE, SIZE), 3)
            if mouse.get_pressed() == (1, 0, 0):
                self.map[int(m.y)][int(m.x)] = self.choose
                self.search = Define(self.map)
                self.huong = self.search.get()
                self.new()
        if mouse.get_pressed() == (1, 0, 0):
            if 0 <= mp[1] < SIZE:
                temp = mp[0] // SIZE
                if temp < len(tap):
                    self.choose = tap[temp]
                    self.choose_img = temp

            if 1240 <= mp[0] <= 1340 and 10 <= mp[1] <= 50:
                self.edit()
            if 1100 <= mp[0] <= 1200 and 10 <= mp[1] <= 50:
                if self.valid():
                    self.saving = True
                else:
                    self.ques = True
            if 1200 <= mp[0] <= 1240 and 10 <= mp[1] <= 50:
                self.running = False
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
    def drawMap(self):
        m = VEC((VEC(mouse.get_pos()).x - VI_TRIX) // SIZE,
                (VEC(mouse.get_pos()).y - VI_TRIY) // SIZE)

        for i in range(WIDTH):
            for j in range(HEIGHT):
                if self.map[j][i] == 2:
                    if m.x == i and m.y == j:
                        self.screen.blit(button_click[0],
                                         (i * SIZE + VI_TRIX, j * SIZE + VI_TRIY))
                    else:
                        self.screen.blit(button[0],
                                         (i * SIZE + VI_TRIX, j * SIZE + VI_TRIY))
                elif self.map[j][i] == 3:
                    if m.x == i and m.y == j:
                        self.screen.blit(button_click[1],
                                         (i * SIZE + VI_TRIX, j * SIZE + VI_TRIY))
                    else:
                        self.screen.blit(button[1],
                                         (i * SIZE + VI_TRIX, j * SIZE + VI_TRIY))
                elif self.map[j][i] == 4:
                    if m.x == i and m.y == j:
                        self.screen.blit(button_click[2],
                                         (i * SIZE + VI_TRIX, j * SIZE + VI_TRIY))
                    else:
                        self.screen.blit(button[2],
                                         (i * SIZE + VI_TRIX, j * SIZE + VI_TRIY))
                elif self.map[j][i] == 5:
                    if m.x == i and m.y == j:
                        self.screen.blit(button_click[3],
                                         (i * SIZE + VI_TRIX, j * SIZE + VI_TRIY))
                    else:
                        self.screen.blit(button[3],
                                         (i * SIZE + VI_TRIX, j * SIZE + VI_TRIY))

    def new(self):
        for i in self.doors:
            i.kill()
        for i in self.sprites:
            i.kill()
        for i in self.monsters:
            i.kill()
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


    def edit(self):
        l = [1, 2, 3, 4, 5]
        for i in range(WIDTH):
            for j in range(HEIGHT):
                if self.map[j][i] == 1:
                    if (j > 0 and self.map[j - 1][i] in l and i > 0 and self.map[j][i - 1] in l) or \
                    (j > 0 and self.map[j - 1][i] in l and i < WIDTH - 1 and self.map[j][i + 1] in l) or \
                    (j < HEIGHT - 1 and self.map[j + 1][i] in l and i > 0 and self.map[j][i - 1] in l) or \
                    (j < HEIGHT - 1 and self.map[j + 1][i] in l and i < WIDTH - 1 and self.map[j][i + 1] in l) :
                        self.map[j][i] = 2

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


    def valid(self):
        temp = []
        for x in range(WIDTH):
            for y in range(HEIGHT):
                temp.append(self.map[y][x])
        if (1 in temp or 2 in temp or 3 in temp or 4 in temp or 5 in temp) and 6 in temp:
            return True
        return False
