from turtle import Turtle
import colors

STARTING_POSITION = (0, -260)
MOVE_INCREMENTAL = 5


class Figure(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(colors.main)
        self.shape("turtle")
        self.setheading(90)
        self.should_move = 0

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def start_move(self):
        self.should_move = 1

    def end_move(self):
        self.should_move = 0

    def update_position(self):
        y_position = self.ycor()
        self.setposition(0, y_position + MOVE_INCREMENTAL * self.should_move)
