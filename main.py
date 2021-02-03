from turtle import Screen
from player import Player
from bullet import Bullet
from enemy import Enemy
from shelter import Shelter
from game import Game
import time
import random

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("SPACE INVADERS")
screen.tracer(0)

game = Game()
player = Player(x_pos=0, y_pos=-250)
sleep_time = 0.02
enemies = []
shelter = []
enemies_moving_right = True


def create_enemies():
    global enemies
    print("Creating enemies")
    start_x = -250
    start_y = 280
    for n in range(5):
        start_y -= 45
        for i in range(11):
            new_enemy = Enemy(x_pos=start_x + i * 45, y_pos=start_y)
            enemies.append(new_enemy)


def create_shelter():
    start_x = 0
    for shelt in range(3):
        start_x = (shelt * 160) - 200
        for n in range(4):
            for i in range(4):
                new_brick = Shelter(x_pos=start_x + i * 20, y_pos=-150 + n * 20)
                shelter.append(new_brick)


create_enemies()
create_shelter()


def fire_bullet():
    global friendly_bullet
    if not friendly_bullet:
        friendly_bullet = Bullet(start_x=player.xcor(), start_y=player.ycor(), friendly=True)


def fire_enemy_bullet(enemy):
    global enemy_bullet
    enemy_bullet = Bullet(start_x=enemy.xcor(), start_y=enemy.ycor(), friendly=False)


def enemy_hit(en):
    en.hideturtle()
    enemies.remove(en)
    game.scoreboard.point(100)


def shelter_hit(brk):
    brk.hideturtle()
    shelter.remove(brk)


def move_enemies():
    global enemies_moving_right
    sorted_by_x = sorted(enemies, key=lambda x: x.xcor(), reverse=True)

    if enemies_moving_right:
        if sorted_by_x[0].xcor() < 265:
            for en in enemies:
                en.move_right()
        else:
            for en in enemies:
                en.move_down()
                enemies_moving_right = False
    else:
        if sorted_by_x[-1].xcor() > -265:
            for en in enemies:
                en.move_left()
        else:
            for en in enemies:
                en.move_down()
                enemies_moving_right = True


screen.listen()
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")
screen.onkey(fire_bullet, "space")

friendly_bullet = None
enemy_bullet = None

game_is_on = True
while game_is_on:
    time.sleep(sleep_time)
    screen.update()

    if friendly_bullet:
        friendly_bullet.move()
        # Check if friendly bullet hits shelter
        for brick in shelter:
            if (abs(friendly_bullet.xcor() - brick.xcor()) < 15) and (
                    abs(friendly_bullet.ycor() - brick.ycor()) < 15):
                friendly_bullet.hideturtle()
                shelter_hit(brick)
                friendly_bullet = None
                break
        # Check if friendly bullet hits enemy
        if friendly_bullet:
            for enemy in enemies:
                if (abs(friendly_bullet.xcor() - enemy.xcor()) < 15) and (
                        abs(friendly_bullet.ycor() - enemy.ycor()) < 15):
                    enemy_hit(enemy)
                    friendly_bullet.hideturtle()
                    friendly_bullet = None
                    break
        # Check if friendly bullet misses everything
        if friendly_bullet:
            if friendly_bullet.ycor() > 310:
                friendly_bullet = None

    if enemy_bullet:
        enemy_bullet.move()
        # Check if enemy bullet hits shelter
        for brick in shelter:
            if (abs(enemy_bullet.xcor() - brick.xcor()) < 15) and (
                    abs(enemy_bullet.ycor() - brick.ycor()) < 15):
                enemy_bullet.hideturtle()
                shelter_hit(brick)
                enemy_bullet = None
                break
        # Check if enemy bullet hits player
        if enemy_bullet:
            if (abs(enemy_bullet.xcor() - player.xcor()) < 15) and (
                    abs(enemy_bullet.ycor() - player.ycor()) < 15):
                enemy_bullet.hideturtle()
                enemy_bullet = None
                game.lose_life()
                if game.scoreboard.lives > 0:
                    player.goto(x=0, y=-250)
                else:
                    player.hideturtle()
                    game_is_on = False
        # Check if enemy bullet misses everything
        if enemy_bullet:
            if enemy_bullet.ycor() < -310:
                enemy_bullet = None
    else:
        fire_enemy_bullet(random.choice(enemies))

    # Check if bullets collide
    if friendly_bullet and enemy_bullet:
        if (abs(friendly_bullet.xcor() - enemy_bullet.xcor()) < 15) and (
                abs(friendly_bullet.ycor() - enemy_bullet.ycor()) < 15):
            friendly_bullet.hideturtle()
            enemy_bullet.hideturtle()
            friendly_bullet = None
            enemy_bullet = None

    move_enemies()

screen.exitonclick()
