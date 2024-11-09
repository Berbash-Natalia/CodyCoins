import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400

cody = Actor('cody')
coin = Actor('coin')
bomb = Actor('bomb')
score = 0


def draw():
    global score
    screen.clear()
    screen.fill((132, 213, 0))
    cody.draw()
    coin.draw()
    if score >= 40:
        bomb.draw()
    if cody.colliderect(bomb):
        score -= 10
        place_bomb()


    screen.draw.text("Cody's coins = " + str(score), topleft=(10, 10), color="black", fontsize=30)


def place_coin():
    coin.x = randint(10, 400)
    coin.y = randint(10, 400)


def place_bomb():
    bomb.x = randint(10, 400)
    bomb.y = randint(10, 400)


def update():
    global score
    speed = 5
    if keyboard.left and cody.x > 40:
        cody.x -= speed
    if keyboard.right and cody.x < 360:
        cody.x += speed
    if keyboard.up and cody.y > 40:
        cody.y -= speed
    if keyboard.down and cody.y < 360:
        cody.y += speed
    if cody.colliderect(coin):
        score += 10
        place_coin()


pgzrun.go()
