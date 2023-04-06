from turtle import Screen
from figure import Figure
from blocks import Blocks
from level import Level
from startscreen import Start_Screen
import colors
import time

# set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor(colors.bg)
screen.tracer(0)  # prevent screen from auto updating

# create start screen
start_screen = Start_Screen()
screen.update()

figure = Figure()  # create play figure
blocks = Blocks()  # create moving blocks
level = Level()  # create level management

screen.listen()

screen.onkeypress(figure.start_move, "Up")  # figure starts moving
screen.onkeyrelease(figure.end_move, "Up")  # figure stops moving

game_is_on = False


def start_game():
    global game_is_on
    if not game_is_on:  # prevent any of those actions if space is pressed while game is running
        game_is_on = True
        figure.showturtle()  # show play figure again
        figure.reset_position()  # reset position of play figure
        start_screen.clear()  # clear start or game over screen
        blocks.init_blocks()  # create new blocks
        level.level = 1  # reset level
        level.update_level()  # write initial level

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
                # wait 1.5 seconds, clear game screen, show game over screen and high score
                game_is_on = False
                time.sleep(1.5)
                blocks.clear_blocks()
                level.show_high_score()
                start_screen.run_again()
                figure.hideturtle()
                screen.update()


screen.onkey(start_game, "space")

screen.exitonclick()
