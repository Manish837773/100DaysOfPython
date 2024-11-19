from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
ball = Ball()

right_paddle = Paddle(380, 0)
left_paddle = Paddle(x=-380, y=0)
right_paddle.speed("fastest")
scoreboard = Scoreboard()


screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

scoreboard.update_scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Scoring
    if ball.xcor() > 400:
        scoreboard.l_score += 1
        scoreboard.update_scoreboard()
        ball.reset_ball()

    if ball.xcor() < -400:
        scoreboard.r_score += 1
        scoreboard.update_scoreboard()
        ball.reset_ball()

    # Detect upper and lower boundary and change the direction
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect paddle touch
    if ((ball.distance(right_paddle) < 50 and ball.xcor() > 350)
            or (ball.distance(left_paddle) < 50 and ball.xcor() < -350)):
        ball.paddle_bounce()
        print("Contact")

screen.exitonclick()
