from turtle import Screen
import time
from ball import Ball
from scoreboard import ScoreBoard
from paddle import Paddle
screen = Screen()
screen.bgcolor("black")
screen.tracer(0)
screen.setup(1000, 600)
paddle1 = Paddle()
paddle1.paddle_position("left")
paddle2 = Paddle()
paddle2.paddle_position("right")
scoreboard = ScoreBoard()
ball = Ball()
is_on = True

while is_on:
    screen.update()
    time.sleep(0.05)
    screen.listen()
    ball.wall_collision()
    ball.start_moving()
    # collision with paddle
    if (ball.distance(paddle1) < 50 or ball.distance(paddle2) < 50) and (ball.xcor() > 430 or ball.xcor() < - 430):
        ball.x_move *= -1

    if ball.xcor() > 500:
        ball.new_ball()
        ball.speed_up()
        scoreboard.score_player1()
    elif ball.xcor() < -500:
        ball.new_ball()
        ball.speed_up()
        scoreboard.score_player2()
    screen.onkey(fun=paddle1.move_paddle_up, key="w")
    screen.onkey(fun=paddle1.move_paddle_down, key="s")
    screen.onkey(fun=paddle2.move_paddle_up, key="Up")
    screen.onkey(fun=paddle2.move_paddle_down, key="Down")

screen.exitonclick()
