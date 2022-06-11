from pygame import *

init()

DISWIDTH = 1366
DISHEIGHT = 768
SIZE = 54

VI_TRIX = 20
VI_TRIY = 100
TITLE = "MY GAME"
FPS = 60
VEC = math.Vector2
VANTOC = 1
FONT = font.Font('font/OhTheHorror.ttf', 30)
FONT1 = font.Font('font/VnArabia.TTF', 30)
# Định nghĩa các vật thể
KEY = {'nothing': 0, 'conveyor': 1, 'arrowu': 2, 'arrowl': 3, 'arrowd': 4, 'arrowr': 5,
       'door': 6, 'sprite1': 7, 'sprite2': 8, 'sprite3': 9, 'sprite4': -9}



WIDTH = 23
HEIGHT = 11
# load anh
door_delay = [transform.scale(image.load('image/door/door_1.png'), (SIZE + 20, SIZE + 20)),
              transform.scale(image.load('image/door/door_2.png'), (SIZE + 20, SIZE + 20))]
mouse_move = image.load('image/mouse/mouse_move.png')
mouse_drag = image.load('image/mouse/mouse_drag.png')
mouse_attack = image.load('image/mouse/mouseclick.png')

door_open = []
for i in range(1, 8, 1):
    door_open.append(transform.scale(image.load('image/door/door_open_{}.png'.format(i)), (SIZE + 20, SIZE + 20)))
door_close = []
for i in range(1, 8, 1):
    door_close.append(transform.scale(image.load('image/door/door_close_{}.png'.format(i)), (SIZE + 20, SIZE + 20)))

stop = [transform.scale(image.load('image/conveyor/stop_1.png'), (SIZE, SIZE)),
        transform.scale(image.load('image/conveyor/stop_2.png'), (SIZE, SIZE))]
up = [transform.scale(image.load('image/conveyor/up_1.png'), (SIZE, SIZE)),
      transform.scale(image.load('image/conveyor/up_2.png'), (SIZE, SIZE)),
      transform.scale(image.load('image/conveyor/up_3.png'), (SIZE, SIZE))]
down = [transform.scale(image.load('image/conveyor/down_1.png'), (SIZE, SIZE)),
        transform.scale(image.load('image/conveyor/down_2.png'), (SIZE, SIZE)),
        transform.scale(image.load('image/conveyor/down_3.png'), (SIZE, SIZE))]
left = [transform.scale(image.load('image/conveyor/left_1.png'), (SIZE, SIZE)),
        transform.scale(image.load('image/conveyor/left_2.png'), (SIZE, SIZE)),
        transform.scale(image.load('image/conveyor/left_3.png'), (SIZE, SIZE))]
right = [transform.scale(image.load('image/conveyor/right_1.png'), (SIZE, SIZE)),
         transform.scale(image.load('image/conveyor/right_2.png'), (SIZE, SIZE)),
         transform.scale(image.load('image/conveyor/right_3.png'), (SIZE, SIZE))]
upleft = [transform.scale(image.load('image/conveyor/upleft_1.png'), (SIZE, SIZE)),
          transform.scale(image.load('image/conveyor/upleft_2.png'), (SIZE, SIZE)),
          transform.scale(image.load('image/conveyor/upleft_3.png'), (SIZE, SIZE))]

upright = [transform.scale(image.load('image/conveyor/upright_1.png'), (SIZE, SIZE)),
           transform.scale(image.load('image/conveyor/upright_2.png'), (SIZE, SIZE)),
           transform.scale(image.load('image/conveyor/upright_3.png'), (SIZE, SIZE))]

leftdown = [transform.scale(image.load('image/conveyor/leftdown_1.png'), (SIZE, SIZE)),
            transform.scale(image.load('image/conveyor/leftdown_2.png'), (SIZE, SIZE)),
            transform.scale(image.load('image/conveyor/leftdown_3.png'), (SIZE, SIZE))]

rightdown = [transform.scale(image.load('image/conveyor/rightdown_1.png'), (SIZE, SIZE)),
             transform.scale(image.load('image/conveyor/rightdown_2.png'), (SIZE, SIZE)),
             transform.scale(image.load('image/conveyor/rightdown_3.png'), (SIZE, SIZE))]

food = [transform.scale(image.load('image/sprites/apple.png'), (SIZE, SIZE)),
        transform.scale(image.load('image/sprites/meat.png'), (SIZE, SIZE)),
        transform.scale(image.load('image/sprites/french_tries.png'), (SIZE, SIZE))]
dream = [transform.scale(image.load('image/sprites/apple_dream.png'), (SIZE, SIZE)),
         transform.scale(image.load('image/sprites/meat_dream.png'), (SIZE, SIZE)),
         transform.scale(image.load('image/sprites/french_tries_dream.png'), (SIZE, SIZE))]

monster = [[transform.scale(image.load('image/dragon/green_dragon_animation/green_dragon_1.png'), (SIZE, SIZE)),
            transform.scale(image.load('image/dragon/green_dragon_animation/green_dragon_2.png'), (SIZE, SIZE)),
            transform.scale(image.load('image/dragon/green_dragon_animation/green_dragon_3.png'), (SIZE, SIZE))],
           [transform.scale(image.load('image/dragon/red_dragon_animation/red_dragon_1.png'), (SIZE, SIZE)),
            transform.scale(image.load('image/dragon/red_dragon_animation/red_dragon_2.png'), (SIZE, SIZE)),
            transform.scale(image.load('image/dragon/red_dragon_animation/red_dragon_3.png'), (SIZE, SIZE))],
           [transform.scale(image.load('image/dragon/white_dragon_animation/white_dragon_1.png'), (SIZE, SIZE)),
            transform.scale(image.load('image/dragon/white_dragon_animation/white_dragon_2.png'), (SIZE, SIZE)),
            transform.scale(image.load('image/dragon/white_dragon_animation/white_dragon_3.png'), (SIZE, SIZE))]
           ]

monster_happy = [
    [transform.scale(image.load('image/dragon/green_dragon_animation/green_dragon_happy_1.png'), (SIZE, SIZE)),
     transform.scale(image.load('image/dragon/green_dragon_animation/green_dragon_happy_2.png'), (SIZE, SIZE)),
     transform.scale(image.load('image/dragon/green_dragon_animation/green_dragon_happy_3.png'), (SIZE, SIZE)),
     transform.scale(image.load('image/dragon/green_dragon_animation/green_dragon_happy_4.png'), (SIZE, SIZE))],
    [transform.scale(image.load('image/dragon/red_dragon_animation/red_dragon_happy_1.png'), (SIZE, SIZE)),
     transform.scale(image.load('image/dragon/red_dragon_animation/red_dragon_happy_2.png'), (SIZE, SIZE)),
     transform.scale(image.load('image/dragon/red_dragon_animation/red_dragon_happy_3.png'), (SIZE, SIZE)),
     transform.scale(image.load('image/dragon/red_dragon_animation/red_dragon_happy_4.png'), (SIZE, SIZE))],
    [transform.scale(image.load('image/dragon/white_dragon_animation/white_dragon_happy_1.png'), (SIZE, SIZE)),
     transform.scale(image.load('image/dragon/white_dragon_animation/white_dragon_happy_2.png'), (SIZE, SIZE)),
     transform.scale(image.load('image/dragon/white_dragon_animation/white_dragon_happy_3.png'), (SIZE, SIZE)),
     transform.scale(image.load('image/dragon/white_dragon_animation/white_dragon_happy_4.png'), (SIZE, SIZE))]
    ]

monster_cry = [[transform.scale(image.load('image/dragon/green_dragon_animation/green_dragon_cry_1.png'), (SIZE, SIZE)),
                transform.scale(image.load('image/dragon/green_dragon_animation/green_dragon_cry_2.png'), (SIZE, SIZE)),
                transform.scale(image.load('image/dragon/green_dragon_animation/green_dragon_cry_1.png'), (SIZE, SIZE)),
                transform.scale(image.load('image/dragon/green_dragon_animation/green_dragon_cry_2.png'),
                                (SIZE, SIZE))],
               [transform.scale(image.load('image/dragon/red_dragon_animation/red_dragon_cry_1.png'), (SIZE, SIZE)),
                transform.scale(image.load('image/dragon/red_dragon_animation/red_dragon_cry_2.png'), (SIZE, SIZE)),
                transform.scale(image.load('image/dragon/red_dragon_animation/red_dragon_cry_3.png'), (SIZE, SIZE)),
                transform.scale(image.load('image/dragon/red_dragon_animation/red_dragon_cry_4.png'), (SIZE, SIZE))],
               [transform.scale(image.load('image/dragon/white_dragon_animation/white_dragon_cry_1.png'), (SIZE, SIZE)),
                transform.scale(image.load('image/dragon/white_dragon_animation/white_dragon_cry_2.png'), (SIZE, SIZE)),
                transform.scale(image.load('image/dragon/white_dragon_animation/white_dragon_cry_3.png'), (SIZE, SIZE)),
                transform.scale(image.load('image/dragon/white_dragon_animation/white_dragon_cry_4.png'), (SIZE, SIZE))]
               ]
monster.append([])
monster_cry.append([])
monster_happy.append([])
for i in range(1, 8):
    monster[3].append(transform.scale(image.load('image/dragon/black_dragon_animation/normal_animation/black{}.png'.format(i)),
                    (SIZE, SIZE)))
    monster_cry[3].append(
        transform.scale(image.load('image/dragon/black_dragon_animation/normal_animation/black{}.png'.format(i)),
                        (SIZE, SIZE)))
    monster_happy[3].append(
        transform.scale(image.load('image/dragon/black_dragon_animation/normal_animation/black{}.png'.format(i)),
                        (SIZE, SIZE)))

button = [transform.scale(image.load('image/button/up.png'), (SIZE, SIZE)),
          transform.scale(image.load('image/button/right.png'), (SIZE, SIZE)),
          transform.scale(image.load('image/button/down.png'), (SIZE, SIZE)),
          transform.scale(image.load('image/button/left.png'), (SIZE, SIZE)),
          transform.scale(image.load('image/button/quit.png'), (SIZE, SIZE)),
          image.load('image/button/create_map.png'),
          image.load('image/button/new_map.png'),
          image.load('image/button/fix.png'),
          image.load('image/button/save.png'),
          image.load('image/button/back.png'),
          image.load('image/button/Continue.png'),
          image.load('image/button/NewGame.png'),
          image.load('image/button/Map.png'),
          image.load('image/button/Option.png'),
          image.load('image/button/Exit.png')]

button_click = [transform.scale(image.load('image/button/up_click.png'), (SIZE, SIZE)),
                transform.scale(image.load('image/button/right_click.png'), (SIZE, SIZE)),
                transform.scale(image.load('image/button/down_click.png'), (SIZE, SIZE)),
                transform.scale(image.load('image/button/left_click.png'), (SIZE, SIZE)),
                transform.scale(image.load('image/button/quit_click.png'), (SIZE, SIZE)),
                image.load('image/button/create_map_click.png'),
                image.load('image/button/new_map_click.png'),
                image.load('image/button/fix_click.png'),
                image.load('image/button/save_click.png'),
                image.load('image/button/back_click.png'),
                image.load('image/button/Continue_Click.png'),
                image.load('image/button/NewGame_Click.png'),
                image.load('image/button/Map_Click.png'),
                image.load('image/button/Option_Click.png'),
                image.load('image/button/Exit_Click.png')]

helicopter1 = []
for i in range(1, 9):
    helicopter1.append(transform.scale(image.load('image/background/maybay1/helicopter{}.png'.format(i)), (100, 30)))

explosion = []
for i in range(9):
    explosion.append(transform.scale(image.load('image/background/explosion/no{}.png'.format(i)), (50, 50)))

slime = [[], [], [], [], [], [], []]
for i in range(1, 4):
    slime[0].append(image.load('image/background/slime/black_slime{}.png'.format(i)))
    slime[1].append(image.load('image/background/slime/blue_slime{}.png'.format(i)))
    slime[2].append(image.load('image/background/slime/green_slime{}.png'.format(i)))
    slime[3].append(image.load('image/background/slime/orange_slime{}.png'.format(i)))
    slime[4].append(image.load('image/background/slime/pink_slime{}.png'.format(i)))
    slime[5].append(image.load('image/background/slime/purple_slime{}.png'.format(i)))
    slime[6].append(image.load('image/background/slime/red_slime{}.png'.format(i)))

background = transform.scale(image.load('image/background/background.png'), (DISWIDTH, DISHEIGHT))
background_minigame1 = transform.scale(image.load('image/background/background_minigame1.png'), (DISWIDTH, DISHEIGHT))

menu_background = transform.scale(image.load('image/background/menu_background.png'), (DISWIDTH, DISHEIGHT))
chosemap = image.load('image/background/map_background.png')
score = image.load('image/background/score.png')
name = image.load('image/background/map_name.png')
question = image.load('image/background/valid.png')
flower = transform.scale(image.load('image/background/flower1.png'), (SIZE, SIZE))
box2 = transform.scale(image.load('image/background/box2.png'), (SIZE, SIZE))
box1 = transform.scale(image.load('image/background/box1.png'), (SIZE, SIZE))
cart1 = transform.scale(image.load('image/background/shopping_cart.png'), (SIZE, SIZE))
bomb = transform.scale(image.load('image/background/bomb.png'), (30 , 10))
bomb2 = transform.scale(image.load('image/background/bomb2.png'), (30 , 10))
tangdiem = transform.scale(image.load('image/background/tangdiem.png'), (20, 20))
trudiem = transform.scale(image.load('image/background/trudiem.png'), (20, 20))
option_frame = transform.scale(image.load('image/background/frame_option.png'), (500 , 292))
dark_frame = image.load('image/background/dark_render.png')
light_frame = image.load('image/background/frame1.png')
music1 = mixer.Sound("sound/horror ambient.ogg")
click = mixer.Sound("sound/zipclick.flac")
music = mixer.Sound('sound/music.wav')
youwin = image.load('image/background/youwin.png')
