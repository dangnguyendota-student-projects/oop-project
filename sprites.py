from pygame import *
from setting import *
from  random import  randrange

def random(x, y):
    a = randrange(0, 2)
    if a == 0:
        return randrange(x, y)
    elif a == 1:
        return -randrange(x, y)

class Door(sprite.Sprite):
    def __init__(self, parent, x, y):
        sprite.Sprite.__init__(self)
        self.parent = parent
        self.image = door_delay[0]
        self.rect = self.image.get_rect()
        self.rect.x = x * SIZE + VI_TRIX - 10
        self.rect.y = y * SIZE + VI_TRIY - 20
        self.time = time.get_ticks()
        self.state = 'delay'
        self.flag = 0
        self.level = 300

    def update(self):
        if self.state == 'delay':
            if sprite.groupcollide(self.parent.doors,self.parent.foods,False,False) :
                self.open()
            if time.get_ticks() - self.time >= self.level:
                self.time = time.get_ticks()
                if self.image == door_delay[0]:
                    self.image = door_delay[1]
                else:
                    self.image = door_delay[0]
        elif self.state == 'open':
            if not sprite.groupcollide(self.parent.doors,self.parent.foods,False,False) and self.flag == 6:
                self.close()
            if time.get_ticks() - self.time >= self.level:
                if self.flag < 6:
                    self.flag += 1
                self.time = time.get_ticks()
                self.image = door_open[self.flag]

        elif self.state == 'close':
            if time.get_ticks() - self.time >= self.level:
                if self.flag < 6:
                    self.flag += 1
                    self.time = time.get_ticks()
                    self.image = door_close[self.flag]
                elif self.flag == 6:
                    self.delay()

    def delay(self):
        self.image = door_delay[0]
        self.state = 'delay'
        self.time = time.get_ticks()
        self.flag = 0

    def open(self):
        self.image = door_open[0]
        self.state = 'open'
        self.time = time.get_ticks()

    def close(self):
        self.image = door_close[0]
        self.state = 'close'
        self.time = time.get_ticks()
        self.flag = 0

class Conveyor(sprite.Sprite):
    def __init__(self,parent,x,y):
        sprite.Sprite.__init__(self)
        self.parent = parent
        self.i = x+y*WIDTH
        self.x = x
        self.y = y
        if self.parent.huong[self.i] == 'doc':
            self.image = stop[0]
        elif self.parent.huong[self.i] == 'ngang':
            self.image = stop[1]
        elif self.parent.huong[self.i] == 'trai':
            self.image = left[0]
        elif self.parent.huong[self.i] == 'phai':
            self.image = right[0]
        elif self.parent.huong[self.i] == 'len':
            self.image = up[0]
        else:
            self.image = down[0]
        self.flag = 0
        self.time = time.get_ticks()
        self.rect = self.image.get_rect()
        self.rect.x = x*SIZE+ VI_TRIX
        self.rect.y = y*SIZE+ VI_TRIY
    def update(self):
        if time.get_ticks() - self.time>500 :
            self.time = time.get_ticks()
            if self.flag<2:
                self.flag += 1
            elif self.flag == 2:
                self.flag = 0
        if self.parent.map[self.y][self.x] == 2 and self.y < HEIGHT-1 and self.x > 0 and\
            self.parent.map[self.y-1][self.x] == self.parent.map[self.y][self.x-1] == 1:
            if (self.y == HEIGHT - 1 or self.parent.map[self.y+1][self.x] != 1 )and \
            (self.x == WIDTH - 1 or self.parent.map[self.y][self.x+1] != 1 ):
                self.image = rightdown[self.flag]
        elif self.parent.map[self.y][self.x] == 2 and self.y > 0 and self.x < WIDTH-1 and \
            self.parent.map[self.y-1][self.x] == self.parent.map[self.y][self.x+1] == 1 :
            if (self.y == HEIGHT-1 or self.parent.map[self.y+1][self.x] != 1 ) and\
            (self.x == 0 or self.parent.map[self.y][self.x-1] != 1 ):
                self.image = leftdown[self.flag]
        elif self.parent.map[self.y][self.x] == 3 and self.y > 0 and self.x < WIDTH-1 and \
            self.parent.map[self.y-1][self.x] == self.parent.map[self.y][self.x+1] == 1:
            if(self.y == HEIGHT-1 or self.parent.map[self.y+1][self.x] != 1) and\
            (self.x == 0 or self.parent.map[self.y][self.x-1] != 1):
                self.image = leftdown[self.flag]
        elif self.parent.map[self.y][self.x] == 3 and self.y < HEIGHT-1 and self.x < WIDTH-1 and \
            self.parent.map[self.y+1][self.x] == self.parent.map[self.y][self.x+1] == 1:
            if(self.y == 0 or self.parent.map[self.y-1][self.x] != 1) and\
            (self.x == 0 or self.parent.map[self.y][self.x-1] != 1):
                self.image = upleft[self.flag]
        elif self.parent.map[self.y][self.x] == 4 and self.y < HEIGHT-1 and self.x > 0 and \
            self.parent.map[self.y+1][self.x] == self.parent.map[self.y][self.x-1] == 1:
            if (self.y == 0 or self.parent.map[self.y-1][self.x] != 1) and\
            (self.x == WIDTH-1 or self.parent.map[self.y][self.x+1] != 1):
                self.image = upright[self.flag]
        elif self.parent.map[self.y][self.x] == 4 and self.y < HEIGHT-1 and self.x < WIDTH-1 and \
            self.parent.map[self.y+1][self.x] == self.parent.map[self.y][self.x+1] == 1:
            if(self.y ==0 or self.parent.map[self.y-1][self.x] != 1) and\
            (self.x == 0 or self.parent.map[self.y][self.x-1] != 1):
                self.image = upleft[len(upleft)-1-self.flag]
        elif self.parent.map[self.y][self.x] == 5 and self.y < HEIGHT-1 and self.x > 0 and \
            self.parent.map[self.y+1][self.x] == self.parent.map[self.y][self.x-1] == 1:
            if(self.y ==0 or self.parent.map[self.y-1][self.x] != 1) and\
            (self.x == WIDTH-1 or self.parent.map[self.y][self.x+1] != 1):
                self.image = upright[self.flag]
        elif self.parent.map[self.y][self.x] == 5 and self.y > 0 and self.x > 0 and \
            self.parent.map[self.y-1][self.x] == self.parent.map[self.y][self.x-1] == 1:
            if(self.y == HEIGHT-1 or self.parent.map[self.y+1][self.x] != 1) and\
            (self.x == WIDTH-1 or self.parent.map[self.y][self.x+1] != 1):
                self.image = rightdown[len(leftdown)-1-self.flag]
        else:
            if self.parent.huong[self.i] == 'doc':
                self.image = stop[0]
            elif self.parent.huong[self.i] == 'ngang':
                self.image = stop[1]
            elif self.parent.huong[self.i] == 'trai':
                self.image = left[self.flag]
            elif self.parent.huong[self.i] == 'phai':
                self.image = right[self.flag]
            elif self.parent.huong[self.i] == 'len':
                self.image = up[self.flag]
            else:
                self.image = down[self.flag]

class Food(sprite.Sprite):
    def __init__(self, parent, x, y, t, v):
        sprite.Sprite.__init__(self)
        self.parent = parent
        self.temp = t
        self.image = food[self.temp]
        self.rect = self.image.get_rect()
        self.rect.x = x*SIZE+ VI_TRIX
        self.rect.y = y*SIZE+ VI_TRIY
        self.vx= 0
        self.vy= 0
        if v == 1:
            self.vantoc = 1
        elif v == 2:
            self.vantoc = 3
        elif v == 3:
            self.vantoc = 6

    def update(self):
        self.rect.x+= self.vx
        self.rect.y+= self.vy
        x = (self.rect.x- VI_TRIX)//SIZE
        y = (self.rect.y- VI_TRIY)//SIZE
        if self.parent.map[y][x] not in [1,2,3,4,5,6]:
            if self.parent.map[y][x] == 0  or self.parent.map[y][x] > 10:
                self.parent.score -= 1
                self.parent.diem.add(Diem(self.rect.center, '-1'))
            self.kill()
            for i in self.parent.monsters:
                if i.x == x and i.y == y:
                    if i.need == self.temp:
                        self.parent.score += 1
                        self.parent.diem.add(Diem(self.rect.center, '+1'))
                        i.happy()
                    else:
                        self.parent.score -= 1
                        self.parent.diem.add(Diem(self.rect.center, '-1'))
                        i.cry()
                    i.need = randrange(0, len(dream))
        if (self.rect.x - VI_TRIX)%SIZE == 0 and (self.rect.y - VI_TRIY)%SIZE == 0 :
            if self.parent.getLenFriend(y, x) > 2:
                if self.parent.map[y][x] == 2:
                    if self.vy > 0 and self.vx == 0:
                        self.parent.score -= 1
                        self.parent.diem.add(Diem(self.rect.center, '-1'))#mini game gi do!
                    self.vx = 0
                    self.vy = -self.vantoc
                elif self.parent.map[y][x] == 3:
                    if self.vy == 0 and self.vx < 0:
                        self.parent.score -= 1
                        self.parent.diem.add(Diem(self.rect.center, '-1'))
                    self.vx = self.vantoc
                    self.vy = 0
                elif self.parent.map[y][x] == 4:
                    if self.vy < 0 and self.vx == 0:
                        self.parent.score -= 1
                        self.parent.diem.add(Diem(self.rect.center, '-1'))
                    self.vx = 0
                    self.vy = self.vantoc
                elif self.parent.map[y][x] == 5:
                    if self.vy == 0 and self.vx > 0:
                        self.parent.score -= 1
                        self.parent.diem.add(Diem(self.rect.center, '-1'))
                    self.vx = -self.vantoc
                    self.vy = 0
            elif self.parent.getLenFriend(y, x) == 2:#gap phai choi re 1 duong duy nhat
                temp = self.parent.getFriend(y, x)
                if self.parent.map[y][x] in [2, 3, 4, 5]:
                    if self.vx != 0 and self.vy == 0:
                        if [y-1, x] in temp:
                            self.vx = 0
                            self.vy = -self.vantoc
                        elif [y+1, x] in temp:
                            self.vx = 0
                            self.vy = self.vantoc
                    elif self.vy != 0 and self.vx == 0 :
                        if [y, x-1] in temp:
                            self.vx = -self.vantoc
                            self.vy = 0
                        elif [y, x+1] in temp:
                            self.vx = self.vantoc
                            self.vy = 0

            if self.parent.map[y][x] == 6:
                if self.parent.door.flag == 6 and self.parent.door.state == 'open':
                    self.vx = 0
                    self.vy = self.vantoc

    def levelUp(self):
        if self.vantoc == 1:
            self.vantoc = 3
        elif self.vantoc == 3:
            self.vantoc = 6
        elif self.vantoc == 6:
            self.vantoc = 1

class Monster(sprite.Sprite):
    def __init__(self,parent,x,y,t):
        sprite.Sprite.__init__(self)
        self.parent = parent
        self.t = t-7
        self.image = monster[t-7][0]
        self.rect = self.image.get_rect()
        self.rect.x = x*SIZE + VI_TRIX
        self.rect.y = y*SIZE + VI_TRIY
        self.x = x
        self.y = y
        self.need = randrange(0,len(dream))
        self.time = time.get_ticks()
        self.state = 'normal'
        self.time_state = time.get_ticks()
        self.flag = 0
    def update(self):
        if self.state == 'normal':
            if time.get_ticks() - self.time_state > 500:
                self.time_state = time.get_ticks()
                if self.flag < len(monster[self.t])-1:
                    self.flag += 1
                elif self.flag == len(monster[self.t])-1:
                    self.flag = 0
            self.image = monster[self.t][self.flag]
        elif self.state == 'cry':
            if time.get_ticks() - self.time_state >500:
                self.time_state = time.get_ticks()
                if self.flag < len(monster_cry[self.t]) - 1:
                    self.flag += 1
                elif self.flag == len(monster_cry[self.t]) - 1:
                    self.normal()
            self.image = monster_cry[self.t][self.flag]
        elif self.state == 'happy':
            if time.get_ticks() - self.time_state >500:
                self.time_state = time.get_ticks()
                if self.flag < len(monster_happy[self.t]) - 1:
                    self.flag += 1
                elif self.flag == len(monster_happy[self.t]) - 1:
                    self.normal()
            self.image = monster_happy[self.t][self.flag]

    def cry(self):
        self.state = 'cry'
        self.time_state = time.get_ticks()
        self.flag = 0
        self.image = monster_cry[self.t][0]
    def happy(self):
        self.state = 'happy'
        self.time_state = time.get_ticks()
        self.flag = 0
        self.image = monster_happy[self.t][0]
    def normal(self):
        self.state = 'normal'
        self.time_state = time.get_ticks()
        self.flag = 0
        self.image = monster[self.t][0]

class Diem(sprite.Sprite):
    def __init__(self, center, kind):
        sprite.Sprite.__init__(self)
        if kind == '+1':
            self.image = tangdiem
        elif kind == '-1':
            self.image = trudiem
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.timeLife = 2000
        self.time = time.get_ticks()
        self.delTa = 0
    def update(self):
        if time.get_ticks() - self.time >= self.timeLife:
            self.kill()
        self.delTa += 0.5
        if self.delTa == 1:
            self.rect.y -= 1
            self.delTa = 0

class Mouse(sprite.Sprite):
    def __init__(self, parent):
        sprite.Sprite.__init__(self)
        self.parent = parent
        self.image = mouse_move
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.attack = False

    def update(self):
        self.mouseEvent()
        self.rect.x = mouse.get_pos()[0]
        self.rect.y = mouse.get_pos()[1]

    def mouseEvent(self):
        m = mouse.get_pressed()
        if not self.attack:
            if m == (1, 0, 0) or m == (1, 0, 1):
                self.image = mouse_drag
            else:
                self.image = mouse_move
        elif self.attack:
            self.image = mouse_attack

class Button(sprite.Sprite):
    def __init__(self, parent, x, y, number):
        sprite.Sprite.__init__(self)
        self.parent = parent
        self.number = number
        self.image = button[number]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.center = self.rect.center

    def update(self):
        if sprite.spritecollide(self, self.parent.mouses, False) and self.rect.y < mouse.get_pos()[1] < self.rect.y + self.rect.height:
            self.image = button_click[self.number]
            self.rect = self.image.get_rect()
            self.rect.center = self.center
        else:
            self.image = button[self.number]
            self.rect = self.image.get_rect()
            self.rect.center = self.center

class Helicopter(sprite.Sprite):
    def __init__(self, x, y, parent):
        sprite.Sprite.__init__(self)
        self.parent = parent
        self.image = helicopter1[0]
        self.vitri = 0
        self.huong = 'trai'
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.time = time.get_ticks()
        self.delay_time_shot = time.get_ticks()
        self.vx = 0
        self.tocgoc = 5
    def update(self):
        if self.rect.x < 0 or self.rect.x > DISWIDTH :
            self.doihuong()
        self.getKey()
        self.animation()
        if self.huong == 'trai':
            self.vx = -self.tocgoc
        elif self.huong == 'phai':
            self.vx = self.tocgoc
        self.rect.x += self.vx

    def animation(self):
        if time.get_ticks() - self.time > 100:
            self.time = time.get_ticks()
            if self.vitri == 3:
                self.vitri = 0
            elif self.vitri == 7:
                self.vitri = 4
            else:
                self.vitri += 1
            self.image = helicopter1[self.vitri]

    def doihuong(self):
        if self.huong == 'trai':
            self.huong = 'phai'
            self.vitri -= 4
            self.image = helicopter1[self.vitri]
        elif self.huong == 'phai':
            self.huong = 'trai'
            self.vitri += 4
            self.image = helicopter1[self.vitri]

    def getKey(self):
        key_state = key.get_pressed()
        if key_state[K_SPACE] and time.get_ticks() - self.delay_time_shot > 1000:
            self.parent.bomb.add(Bomb(self.rect.x + self.rect.width//2, self.rect.y + self.rect.height//2, self.vx, self.parent))
            self.delay_time_shot = time.get_ticks()
        if key_state[K_LEFT] and self.huong == 'phai':
            self.doihuong()
        elif key_state[K_RIGHT] and self.huong == 'trai':
            self.doihuong()

class Bomb (sprite.Sprite):
    def __init__(self, x, y, vx, parent):
        sprite.Sprite.__init__(self)
        if vx > 0:
            self.image = bomb
        else:
            self.image = bomb2
        self.parent = parent
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.giatoc = 0.15
        self.vx = vx
        self.vy = 0

    def update(self):
        if sprite.spritecollide(self, self.parent.monster, True):
            self.parent.effect.add(Explosion(self.rect.x, self.rect.y))#va cham voi slime
            self.kill()
        self.rect.x += self.vx
        self.rect.y += self.vy
        self.vy += self.giatoc
        if self.rect.y > DISHEIGHT - 120:
            self.kill()
            self.parent.effect.add(Explosion(self.rect.x, self.rect.y))

class Explosion(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.vitri = 0
        self.image = explosion[self.vitri]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.deltaTime = 100
        self.time = time.get_ticks()
    def update(self):
        self.animation()

    def animation(self):
        if time.get_ticks() - self.time > self.deltaTime:
            self.time = time.get_ticks()
            if self.vitri == 8:
                self.kill()
            elif self.vitri < 8:
                self.vitri += 1
                self.image = explosion[self.vitri]

class Slime(sprite.Sprite):
    def __init__(self, x, y, parent):
        sprite.Sprite.__init__(self)
        self.parent = parent
        self.vitri = 0
        self.slime_so = randrange(7)
        self.time_animation = time.get_ticks()
        self.time_move = time.get_ticks()
        self.delta_time_move = randrange(2000, 10000)
        self.vx = random(1, 4)
        self.deltaTime = 200
        self.image = slime[self.slime_so][self.vitri]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.animation()
        self.move()

    def animation(self):
        if time.get_ticks() - self.time_animation > self.deltaTime:
            self.time_animation = time.get_ticks()
            if self.vitri == 2:
                self.vitri = 0
            else:
                self.vitri += 1
            self.image = slime[self.slime_so][self.vitri]
    def move(self):
        if time.get_ticks() - self.time_move > self.delta_time_move or \
            self.rect.x >= DISWIDTH - self.rect.width or\
            self.rect.x <= 0 :
            self.time_move = time.get_ticks()
            self.delta_time_move = randrange(2000, 10000)
            if self.vx > 0:
                self.vx = -randrange(1, 4)
            else:
                self.vx = randrange(1, 4)
        self.rect.x += self.vx

class winGame(sprite.Sprite):
    def __init__(self, parent):
        self.parent = parent
        sprite.Sprite.__init__(self)
        self.image=transform.scale(youwin,(10,10))
        self.rect=self.image.get_rect()
        self.rect.center=[600, 400]
        self.tf=10
        self.time=time.get_ticks()
        self.width=10

    def update(self):
        if time.get_ticks()-self.time>50 and self.width<200:
            self.time=time.get_ticks()
            self.width+=10
            self.image=transform.scale(youwin,(self.width,self.width))
            self.rect = self.image.get_rect()
            self.rect.center = [600, 400]
        elif time.get_ticks() - self.time > 1000 and self.parent.level_campaign < 5:
            self.kill()
            self.parent.quaMan()
