import pygame as pg  # если импортируется модуль с длинным именем то его можно сократить до псевдонима при помощи as
import random
from pygame.locals import *  # это не особо хорошая конструкция потому что мы не знаем точно какие имена импортировались

# при помощи конструкции from <'module_name'> import <'name'> можно импортировать конкретные функции
# или константы, если написать from <'module_name'> import * то импортируется всё, что есть в этом модуле
DISPLAYWIDTH = 800
STONEWIDTH = 106
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((800, 600))
background = pg.image.load('background.jpg')
music = pg.mixer.music.load('KIDS.mp3')
stoneImg = pg.image.load('stone.png')
enemyImg = pg.image.load('enemy.png')
stoneX = 380
stoneY = 315
enemyX = 0
enemyY = 0
stoneX_change = 0  # изменяя численное значение этого параметра можно влиять на скорость и направление перемещения



# поменять фон
# добавить врага камня

def stone(x, y):
    screen.blit(stoneImg, (x, y))


running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    # событием называется любое действие пользователя внутри заданного окна (движение курсора, нажатия клавиш,
    # взаимодействие с кнопками
    for event in pg.event.get():  # вызов этого метода возвращает список, по которому мы в последствии проходимся
        if event.type == QUIT:  # у объектов event есть "тип" (атрибут под названием type) который позволяет понять
            # какое конкретно событие произошло
            running = False
        if event.type == KEYDOWN:
            # print('Клавиша нажата')
            if event.key == K_LEFT:  # можно было выбрать любые другие клавиши
                stoneX_change = -2  # когда будет зажата и удерживаться левая стрелка
            if event.key == K_RIGHT:
                stoneX_change = 2  # когда будет зажата и удерживаться правая стрелка
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                stoneX_change = 0

    stoneX += stoneX_change  # координата камня будет меняться когда будет зажата какая-то из стрелок
    if stoneX <= 0:
        stoneX = 0
    if stoneX >= DISPLAYWIDTH - STONEWIDTH:  # при помощи этого выражения мы делаем так чтобы самая правая
        # граница камня не могла заехать за границу окна
        stoneX = DISPLAYWIDTH - STONEWIDTH
    stone(stoneX, stoneY)
    pg.display.update()
