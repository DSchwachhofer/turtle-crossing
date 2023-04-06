from turtle import Screen
from figure import Figure
from blocks import Blocks
from level import Level
from startscreen import Start_Screen
import colors
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor(colors.bg)
screen.tracer(0)

start_screen = Start_Screen()
screen.update()

screen.listen()

figure = Figure()
blocks = Blocks()
level = Level()

screen.onkeypress(figure.start_move, "Up")
screen.onkeyrelease(figure.end_move, "Up")

game_is_on = False


def start_game():
    global game_is_on
    if not game_is_on:
        figure.showturtle()
        start_screen.clear()
        game_is_on = True
        figure.reset_position()
        level.level = 0
        level.update_level()
        blocks.init_blocks()

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
                time.sleep(1.5)
                blocks.clear_blocks()
                level.show_high_score()
                start_screen.run_again()
                figure.hideturtle()
                screen.update()


screen.onkey(start_game, "space")

screen.exitonclick()
