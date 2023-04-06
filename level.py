from turtle import Turtle
import colors


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color(colors.main)
        self.hideturtle()
        self.penup()
        self.setposition(-280, 240)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"level: {self.level}", align="left", font=("Menlo", 40, "normal"))
        self.level += 1
