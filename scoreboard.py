from turtle import Turtle

FONT = ("Courier", 16, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.point = 0
        self.penup()
        self.hideturtle()
        self.goto(-230, 260)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.point}", align="center", font=FONT)

    def increment(self):
        self.clear()
        self.point += 1
        self.update_score()

    def gameover(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
