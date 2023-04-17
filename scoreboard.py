from display import MyScreen
from turtle import Turtle

# Declare variable and CONSTANT
LEVEL_SCORE = 3
DISTANCE_FOR_SCORE = 60
GAME_OVER_IMAGE = "./image/snake.png"
FONT = ("Courier", 15, "bold")
ALIGN = "center"


# Class Scoreboard
class Scoreboard(Turtle):
    """
    Class Scoreboard
    Instance:
    score, level, level_speed
    Method:
    game_over, increase_score,
    increase_leve, refresh_score
    """
    def __init__(self):
        super().__init__()
        self.score = 0
        self.level = 0
        self.level_speed = 0.1
        self.color("#FFFFFF")
        self.penup()
        self.hideturtle()
        self.goto(0, MyScreen().y_coord - DISTANCE_FOR_SCORE)
        self.refresh_score()

    def game_over(self):
        self.goto(0, 0)
        MyScreen().this_window.bgpic(GAME_OVER_IMAGE)
        self.write(f"GAME OVER", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1

    def increase_level(self):
        if self.score % LEVEL_SCORE == 0:
            self.level += 1
            self.level_speed *= 0.9

    def refresh_score(self):
        self.clear()
        self.write(f"Level: {self.level} \t Score: {self.score}", align=ALIGN, font=FONT)
