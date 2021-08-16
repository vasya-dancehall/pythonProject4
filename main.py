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
bulletImg = pg.image.load('bullet.png')
bulletX = 0
bulletY = 315
bulletY_change = -2
bullet_state = 'ready'
stoneX = 380
stoneY = 315
enemyX = 0
enemyY = 220
stoneX_change = 0  # изменяя численное значение этого параметра можно влиять на скорость и направление перемещения
enemyX_change = 0.5


def stone(x, y):
    screen.blit(stoneImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10))

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
            if event.key == K_SPACE:
                if bullet_state is 'ready':
                    bulletX = stoneX
                    fire_bullet(bulletX, bulletY)

        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                stoneX_change = 0

    stoneX += stoneX_change  # координата камня будет меняться когда будет зажата какая-то из стрелок
    enemyX += enemyX_change
    if stoneX <= 0:
        stoneX = 0
    if stoneX >= DISPLAYWIDTH - STONEWIDTH:  # при помощи этого выражения мы делаем так чтобы самая правая
        # граница камня не могла заехать за границу окна
        stoneX = DISPLAYWIDTH - STONEWIDTH
    if enemyX <= 0:
        enemyX = 0
        enemyX_change = 0.5
    if enemyX >= DISPLAYWIDTH - 80:
        enemyX = DISPLAYWIDTH - 80
        enemyX_change = -0.5
    if bulletY <= 0:
        bulletY = 315
        bullet_state = 'ready'
    if bullet_state is 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY += bulletY_change

    stone(stoneX, stoneY)
    enemy(enemyX, enemyY)
    pg.display.update()
