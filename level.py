from turtle import Turtle
import colors

FONT = ("Menlo", 25, "normal")


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.high_score = 0
        self.color(colors.main)
        self.hideturtle()
        self.penup()

    def update_level(self):
        self.clear()
        self.setposition(-280, 250)
        self.write(f"level: {self.level}", align="left", font=FONT)
        self.level += 1

    def show_high_score(self):
        if self.level > self.high_score:
            self.high_score = self.level - 1
        self.setposition(270, 250)
        self.write(f"high score: {self.high_score}", align="right", font=FONT)
