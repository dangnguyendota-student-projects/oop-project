from setting import  *
from  sprites import  *
from pygame import *

class MiniGame_1:
    def __init__(self):
        init()
        mixer.init()
        self.clock = time.Clock()
        display.set_caption(TITLE)
        mouse.set_visible(False)
        self.time = time.get_ticks()
        self.music = True

    def new(self):
        self.screen = display.set_mode((DISWIDTH, DISHEIGHT))
        self.running = True
        self.all_sprite = sprite.Group()
        self.helicopter = sprite.Group()
        self.bomb = sprite.Group()
        self.monster = sprite.Group()
        self.effect = sprite.Group()

        self.helicopter.add(Helicopter(0, 50, self))
        self.monster.add(Slime(DISWIDTH//2, DISHEIGHT - 200, self))
        self.monster.add(Slime(DISWIDTH // 2, DISHEIGHT - 200, self))
        self.monster.add(Slime(DISWIDTH // 2, DISHEIGHT - 200, self))
        self.monster.add(Slime(DISWIDTH // 2, DISHEIGHT - 200, self))

    def run(self):
        while self.running:
            self.event()
            self.update()
            self.collision()
            self.draw()
            display.update()
            self.clock.tick()

    def event(self):
        for e in event.get():
            if e.type == QUIT:
                quit()
                exit()

    def update(self):
        self.all_sprite.update()
        self.helicopter.update()
        self.bomb.update()
        self.monster.update()
        self.effect.update()

    def collision(self):
        pass

    def draw(self):
        self.screen.blit(background_minigame1, (0, 0))
        self.all_sprite.draw(self.screen)
        self.bomb.draw(self.screen)
        self.helicopter.draw(self.screen)
        self.monster.draw(self.screen)
        self.effect.draw(self.screen)

m = MiniGame_1()
m.new()
m.run()