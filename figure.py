from turtle import Turtle
import colors


class Figure(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(colors.main)
        self.shape("turtle")
        self.setheading(90)
        self.reset_position()

    def reset_position(self):
        self.goto(0, -260)

    def move(self):
        self.forward(10)
