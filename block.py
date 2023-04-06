from turtle import Turtle
import colors
import random


# class for one single block
class Block(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(random.choice(colors.blocks))
        self.shape("square")
        self.shapesize(1, 2)
        self.init_block()

    # when game starts and levels up, blocks are placed randomly on game screen
    def init_block(self):
        self.showturtle()
        self.setposition(random.randint(-300, 600), random.randint(-200, 230))

    # when blocks are out of screen, they are randomly positioned beyond right side of screen
    def reset(self):
        self.setposition(random.randint(300, 600), random.randint(-200, 230))

    def move(self, level):
        self.setposition(self.xcor() - level / 4 - 2, self.ycor())  # moves block and increases speed with level up
        if self.xcor() < -350:
            self.reset()
