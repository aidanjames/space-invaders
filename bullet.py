from turtle import Turtle


class Bullet(Turtle):

    def __init__(self, start_x, start_y, friendly):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=0.7, stretch_len=0.3)
        self.penup()
        self.goto(start_x, start_y)
        self.friendly = friendly
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.1

    def move(self):
        if self.friendly:
            new_y = self.ycor() + self.y_move
        else:
            new_y = self.ycor() - self.y_move

        self.goto(self.xcor(), new_y)
