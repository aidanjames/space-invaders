from turtle import Turtle


class Enemy(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.color("white")
        self.shape("turtle")
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.right(90)
        self.penup()
        self.goto(x_pos, y_pos)

    def move_left(self):
        if self.xcor() >= -270:
            new_x = self.xcor() - 0.5
            self.goto(new_x, self.ycor())

    def move_right(self):
        if self.xcor() <= 270:
            new_x = self.xcor() + 0.5
            self.goto(new_x, self.ycor())

    def move_down(self):
        if self.ycor() >= -270:
            new_y = self.ycor() - 1
            self.goto(self.xcor(), new_y)

