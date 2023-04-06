from turtle import Turtle
import colors


class Figure(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(colors.main)
        self.shape("turtle")
        self.setheading(90)
        self.should_move = 0
        self.reset_position()

    def reset_position(self):
        self.goto(0, -260)

    def start_move(self):
        self.should_move = 1

    def end_move(self):
        self.should_move = 0

    def update_position(self):
        y_position = self.ycor()
        self.setposition(0, y_position + 5 * self.should_move)
