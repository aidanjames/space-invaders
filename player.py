from turtle import Turtle
from bullet import Bullet


class Player(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.penup()
        self.goto(x_pos, y_pos)
        self.right(270)

    def move_left(self):
        if self.xcor() >= -270:
            new_x = self.xcor() - 20
            self.goto(new_x, self.ycor())

    def move_right(self):
        if self.xcor() <= 270:
            new_x = self.xcor() + 20
            self.goto(new_x, self.ycor())





