from turtle import Turtle


class Shelter(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.color("green")
        self.shape("square")
        self.penup()
        self.goto(x_pos, y_pos)
