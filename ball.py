from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = 10
        self.y_move = 10

    def start_moving(self):
        self.goto(self.xcor() + self.x_move, self.ycor()+self.y_move)

    def wall_collision(self):
        if self.ycor() > 280 or self.ycor() < - 280:
            self.y_move *= -1

    def new_ball(self):
        self.goto(0, 0)

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()

    def speed_up(self):
        self.x_move += 2
        self.y_move += 2
