import pgzrun
from random import randint

WIDTH = 500
HEIGHT = 500

cody = Actor('cody')
coin = Actor('coin')


def draw():
    screen.clear()
    screen.fill((0, 191, 255))
    cody.draw()


def place_coin():
    coin.x = randint(10, 300)
    coin.y = randint(10, 300)


def update():
    global score
    speed = 5
    if keyboard.left:
        cody.x -= speed
    if keyboard.right:
        cody.x += speed
    if keyboard.up:
        cody.y -= speed
    if keyboard.down:
        cody.y += speed





pgzrun.go()
