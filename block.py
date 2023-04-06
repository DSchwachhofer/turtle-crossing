from turtle import Turtle
import colors
import random


class Block(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(colors.blocks[random.randint(0, 2)])
        self.shape("square")
        self.shapesize(1, 2)
        self.init_block()

    def init_block(self):
        self.setposition(random.randint(-300, 600), random.randint(-200, 230))

    def reset(self):
        self.setposition(random.randint(300, 600), random.randint(-200, 230))

    def move(self, level):
        self.setposition(self.xcor() - level / 4 - 2, self.ycor())
        if self.xcor() < -350:
            self.reset()
