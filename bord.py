import display
from display import MyScreen
from turtle import Turtle

# Declare variable and CONSTANT
DISTANCE = 20
DISTANCE_COORD = 10
BORD_COLOR = "#AAAFFF"
PENSIZE = 10


# Class BordGame
class BordGame(Turtle):
    """ Class BordGame"""
    def __init__(self):
        super().__init__()
        self.goto(-MyScreen().x_coord + DISTANCE_COORD, MyScreen().y_coord - DISTANCE_COORD)
        self.color(BORD_COLOR)
        self.pensize(PENSIZE)
        self.hideturtle()
        self.speed("fastest")

    # Method to create bord
    def create_bord(self):
        """Method to create bord"""
        for i in range(4):
            self.forward(display.X_SCREEN - DISTANCE)
            self.right(90)
            self.forward(display.Y_SCREEN - DISTANCE)
            self.right(90)
