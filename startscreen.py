from turtle import Turtle
import colors
import art


class Start_Screen(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color(colors.main)
        self.start()

    def start(self):
        self.setposition(0, -100)
        self.write(art.logo, align="center", font=("Menlo", 14, "normal"))
        self.setposition(0, -190)
        self.write("use up arrow to move turtle", align="center", font=("Menlo", 20, "normal"))
        self.setposition(0, -240)
        self.write("PRESS SPACE TO START GAME", align="center", font=("Menlo", 28, "normal"))

    def run_again(self):
        self.setposition(0, -100)
        self.write(art.game_over, align="center", font=("Menlo", 14, "normal"))
        self.setposition(0, -240)
        self.write("PRESS SPACE TO RUN GAME AGAIN", align="center", font=("Menlo", 28, "normal"))
