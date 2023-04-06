from turtle import Screen
from figure import Figure
from blocks import Blocks
from level import Level
import colors
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor(colors.bg)
screen.tracer(0)

figure = Figure()
blocks = Blocks()
level = Level()

screen.listen()
screen.onkeypress(figure.start_move, "Up")
screen.onkeyrelease(figure.end_move, "Up")

game_is_on = True


def end_game():
    global game_is_on
    game_is_on = False
    print("Goodbye")


screen.onkey(end_game, "Escape")
while game_is_on:
    screen.update()
    time.sleep(0.01)

    figure.update_position()
    blocks.move(level.level)

    # detect when figure has reached finish
    if figure.ycor() > 260:
        figure.reset_position()
        level.update_level()
        blocks.reset()

    # detect collision with blocks
    if blocks.check_collision(figure.ycor()):
        game_is_on = False
        print("GAME OVER")

screen.exitonclick()
