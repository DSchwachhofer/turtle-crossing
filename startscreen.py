from turtle import Turtle
import colors
import art

FONT = "Menlo"


def set_font_spec(size):
    spec = (FONT, size, "normal")
    return spec


class Start_Screen(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color(colors.main)
        self.start()

    def start(self):
        self.setposition(0, -100)
        self.write(art.logo, align="center", font=set_font_spec(14))
        self.setposition(0, -190)
        self.write("use up arrow to move turtle", align="center", font=set_font_spec(20))
        self.setposition(0, -240)
        self.write("PRESS SPACE TO START GAME", align="center", font=set_font_spec(28))

    def run_again(self):
        self.setposition(0, -100)
        self.write(art.game_over, align="center", font=set_font_spec(14))
        self.setposition(0, -240)
        self.write("PRESS SPACE TO RUN GAME AGAIN", align="center", font=set_font_spec(28))
