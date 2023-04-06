from turtle import Screen
from figure import Figure
import colors
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor(colors.bg)
screen.tracer(0)

figure = Figure()

screen.listen()
screen.onkey(figure.move, "Up")

game_is_on = True


def end_game():
    global game_is_on
    game_is_on = False
    print("Goodbye")


screen.onkey(end_game, "Escape")
while game_is_on:
    screen.update()
    time.sleep(0.01)

    # detect when figure has reached finish
    if figure.ycor() > 260:
        figure.reset_position()

screen.exitonclick()
