import pgzrun
import sys
from random import randint

TITLE="Cody's Coins"

WIDTH = 400
HEIGHT = 400

cody = Actor('cody')
coin = Actor('coin')
cody.x=200
cody.y=200
coin.x = randint(10, 400)
coin.y = randint(10, 400)
score = 0

game_over = False

beep = tone.create('E3', 0.5)




def draw():
    if game_over:
        screen.fill((225,99,19))
        screen.draw.text("The end! :( ", topleft=(10, 60), fontsize=60)
        screen.draw.text("Cody's coins = : " + str(score), color="black", topleft=(10, 10), fontsize=60)
    else:
        screen.clear()
        screen.fill((132, 213, 0))
        cody.draw()
        coin.draw()
        screen.draw.text("Cody's coins = " + str(score), topleft=(10, 10), color="black", fontsize=30)


def place_coin():
    coin.x = randint(10, 400)
    coin.y = randint(10, 400)


def the_end():
    global game_over
    game_over = True



def update():
    global score
    speed = 5
    if game_over:
        # Прекращаем обновление игры, если игра завершена
        return

    if keyboard.A and cody.x > 40:
        cody.x -= speed
    if keyboard.D and cody.x < 360:
        cody.x += speed
    if keyboard.W and cody.y > 40:
        cody.y -= speed
    if keyboard.S and cody.y < 360:
        cody.y += speed
    if cody.colliderect(coin):
        score += 10
        place_coin()

clock.schedule_unique(the_end, 6.0)
pgzrun.go()
