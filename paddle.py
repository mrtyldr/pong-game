from turtle import Turtle


class Paddle(Turtle):

    def __init__(self,):
        super().__init__()
        self.shape("square")
        self.right(90)
        self.shapesize(stretch_len=5)
        self.color("white")
        self.penup()

    def paddle_position(self, position):

        if position == "left":
            self.goto(-450, 0)
        elif position == "right":
            self.goto(450, 0)

    def move_paddle_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_paddle_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
