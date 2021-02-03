from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 3
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-220, 255)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 20, "normal"))
        self.goto(200, 255)
        self.write(f"Lives: {self.lives}", align="center", font=("Courier", 20, "normal"))

    def point(self, points):
        self.score += points
        self.update_scoreboard()

    def lose_life(self):
        self.lives -= 1
        self.update_scoreboard()