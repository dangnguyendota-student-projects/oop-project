from setting import *
from sprites import *
from  main import Game
from createmap import createmap

class menu():
    def __init__(self, g, c):
        init()
        mixer.init()
        self.clock = time.Clock()
        display.set_caption(TITLE)
        mouse.set_visible(False)
        self.g = g
        self.pick = 0
        self.music = True
        self.play = False
        self.option = False
        self.game_type = 0
        self.level = 1
        self.createMap = c
        with open('map/musicOption.txt', 'r') as lines:
            for line in lines:
                if int(line) == 0:
                    self.music = True
                    self.g.music = True
                else:
                    self.music = False
                    self.g.music = False
        with open('map/Level.txt', 'r') as lines:
            for line in lines:
                self.level = int(line)
            self.g.v = self.level
        with open('map/Map.txt', 'r') as lines:
            for line in lines:
                self.pick = int(line)
        with open('map/gameType.txt', 'r') as lines:
            for line in lines:
                self.game_type = int(line)
    def new(self):
        self.screen = display.set_mode((DISWIDTH, DISHEIGHT))
        self.mouses = sprite.Group()
        self.buttons = sprite.Group()
        self.mouses.add(Mouse(self))
        self.newButton()
        self.running = True
        self.choseMap = False
        self.map = []
        self.link = []

        with open('map/link.txt', 'r') as lines:
            for line in lines:
                self.link.append(line.split())

        for i in range(len(self.link)):
            self.map.append([])
            with open(str(self.link[i][0]), 'r') as lines:
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

                    self.map[i].append(temp)

        self.map_campaign = []
        with open('map/level1.txt', 'r') as lines:
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

                self.map_campaign.append(temp)


    def showMenu(self):
        music1.play(-1)
        if not self.music:
            music1.set_volume(0)
        else:
            music1.set_volume(1)
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
                if e.key == K_ESCAPE:
                    quit()
                    exit()
                if e.key == K_RETURN :
                    if self.choseMap:
                        self.choseMap = False
                    if self.option:
                        self.option = False
            if e.type == MOUSEBUTTONDOWN and not self.choseMap and not self.option:
                m = mouse.get_pos()
                if e.button == 1 and 0 <= m[0] <= 400:
                    if 100 <= m[1] <= 200 and self.play:
                        self.running = False  # continue
                        self.g.running = True
                        self.g.run()
                    if 220 <= m[1] <= 320:
                        music1.set_volume(0)
                        self.play = True
                        self.running = False  # new game
                        if self.game_type == 1:
                            self.g.new(self.map[self.pick], 'modern', 1)
                            self.g.run()
                        elif self.game_type == 0:
                            self.g.new(self.map_campaign, 'campaign', 1)
                            self.g.run()
                    if 340 <= m[1] <= 440: # choose map
                        self.running = False
                        self.createMap.newMap()
                        self.createMap.run()

                    if 460 <= m[1] <= 560:
                        self.running = False  # option
                        self.option = True

                    if 580 <= m[1] <= 680:
                        quit()
                        exit()  # quit

            if e.type == MOUSEBUTTONDOWN and self.option:#dang trong chon map
                if e.button == 1:
                    if self.game_type == 1:
                        if 630 < mouse.get_pos()[0] < 684 and 310 < mouse.get_pos()[1] < 364 and self.pick > 0:#chon map
                            self.pick -= 1
                            self.setValue("Map", self.pick)
                            self.play = False  # khong tiep tuc duoc nua
                        elif 930 < mouse.get_pos()[0] < 984 and 310 < mouse.get_pos()[1] < 364 and self.pick < len(self.link) - 1:
                            self.pick += 1
                            self.setValue("Map", self.pick)
                            self.play = False  # khong tiep tuc duoc nua
                    if 500 < mouse.get_pos()[0] < 1000 and 520 < mouse.get_pos()[1] < 570:#thoat khoi tuy chinh
                        self.option = False
                    elif 500 < mouse.get_pos()[0] < 1000 and 370 < mouse.get_pos()[1] < 420:#thay doi level choi
                        if self.level == 3:
                            self.level = 1
                            self.setValue("Level", 1)
                        else:
                            self.level += 1
                            self.setValue("Level", self.level)
                        self.g.levelUp()
                        self.play = False  # khong tiep tuc duoc nua
                    elif 500 < mouse.get_pos()[0] < 1000 and 420 < mouse.get_pos()[1] < 470:# thay doi che do choi
                        if self.game_type == 0:
                            self.game_type = 1
                            self.setValue("gameType", 1)
                        else:
                            self.game_type = 0
                            self.setValue("gameType", 0)
                        self.play = False #khong tiep tuc duoc nua
                    elif 500 < mouse.get_pos()[0] < 1000 and 470 < mouse.get_pos()[1] < 520:#tuy chinh am thanh
                        if self.music:
                            self.music = False
                            self.g.music = False
                            music1.set_volume(0)
                            self.setValue("musicOption", 1)
                        else:
                            self.music = True
                            self.g.music = True
                            music1.set_volume(1)
                            self.setValue("musicOption", 0)


    def update(self):
        self.mouses.update()
        self.buttons.update()
        display.set_caption(str(mouse.get_pos()))


    def draw(self):
        self.screen.fill(Color('white'))
        self.screen.blit(menu_background, (0, 0))
        self.buttons.draw(self.screen)
        if self.option:#dang trong tuy chon
            self.screen.blit(dark_frame, (0, 0))
            if 500 < mouse.get_pos()[0] < 1000 and 320 < mouse.get_pos()[1] < 370:
                self.screen.blit(light_frame, (500, 320))
            elif 500 < mouse.get_pos()[0] < 1000 and 370 < mouse.get_pos()[1] < 420:
                self.screen.blit(light_frame, (500, 370))
            elif 500 < mouse.get_pos()[0] < 1000 and 420 < mouse.get_pos()[1] <470:
                self.screen.blit(light_frame, (500, 420))
            elif 500 < mouse.get_pos()[0] < 1000 and 470 < mouse.get_pos()[1] < 520:
                self.screen.blit(light_frame, (500, 470))
            elif 500 < mouse.get_pos()[0] < 1000 and 520 < mouse.get_pos()[1] < 570:
                self.screen.blit(light_frame, (500, 520))
            if self.game_type == 1:
                if 630 < mouse.get_pos()[0] < 684 and 310 < mouse.get_pos()[1] < 364 :
                    self.screen.blit(button_click[3], (630, 310))
                else:
                    self.screen.blit(button[3], (630, 310))
                if 930 < mouse.get_pos()[0] < 984 and 310 < mouse.get_pos()[1] < 364:
                    self.screen.blit(button_click[1], (930, 310))
                else:
                    self.screen.blit(button[1], (930, 310))
            text1 = FONT1.render("Map :", True, Color('yellow'), None)
            text2 = FONT1.render("Level :", True, Color("yellow"), None)
            text3 = FONT1.render("Game type :", True, Color("yellow"), None)
            text4 = FONT1.render("Music :", True, Color("yellow"), None)
            text5 = FONT1.render("OK!", True, Color("yellow"), None)
            on = FONT1.render("ON", True, Color("red"), None)
            off = FONT1.render("OFF", True, Color("red"), None)
            type1 = FONT1.render("campaign", True, Color("red"), None)
            type2 = FONT1.render("modern", True, Color("red"), None)
            level1 = FONT1.render("Easy", True, Color("red"), None)
            level2 = FONT1.render("Normal", True, Color("red"), None)
            level3 = FONT1.render("Hard", True, Color("red"), None)
            map_str = str(self.link[self.pick][0])
            map_str = map_str[4: len(map_str) - 4]
            map_name = FONT1.render(map_str, True, (255, 0, 0), None)
            if self.game_type == 1:
                self.screen.blit(text1, (550, 320))
            self.screen.blit(text2, (550, 370))
            self.screen.blit(text3, (550, 420))
            self.screen.blit(text4, (550, 470))
            self.screen.blit(text5, (700, 520))
            if self.music :
                self.screen.blit(on, (720, 470))
            else:
                self.screen.blit(off, (720, 470))
            if self.game_type == 0:
                self.screen.blit(type1, (720, 420))
            elif self.game_type == 1:
                self.screen.blit(type2, (720, 420))
            if self.level == 1:
                self.screen.blit(level1, (720, 370))
            elif self.level == 2:
                self.screen.blit(level2, (720, 370))
            elif self.level == 3:
                self.screen.blit(level3, (720, 370))
            if self.game_type == 1:
                self.screen.blit(map_name, (690, 320))
            self.screen.blit(option_frame, (500, 300))

        self.mouses.draw(self.screen)

    def newButton(self):
        self.buttons.add(Button(self, 50, 100, 10))
        self.buttons.add(Button(self, 50, 220, 11))
        self.buttons.add(Button(self, 50, 340, 12))
        self.buttons.add(Button(self, 50, 460, 13))
        self.buttons.add(Button(self, 50, 580, 14))

    def showChoseMapMenu(self):
        pass

    def setValue(self, file, value):
        f = open('map/'+file+'.txt', 'w')
        f.write(str(value))
        f.close()

c = createmap()
g = Game()
m = menu(g, c)

while True:
    m.new()
    m.showMenu()
