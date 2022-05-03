from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.player1 = 0
        self.player2 = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 200)
        self.write_score()

    def score_player1(self):
        self.player1 += 1
        self.write_score()

    def score_player2(self):
        self.player2 += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg=f"{self.player1} : {self.player2}", align="center", font=("courier", 50, "normal"))
