from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.shapesize(1, 1)
        self.shape("square")
        self.penup()
        self.x_delta = 10
        self.y_delta = 10
        self.move_speed = 0.07

    def move(self):
        x = self.xcor() + self.x_delta
        y = self.ycor() + self.y_delta
        self.goto(x, y)

    # Direction change of the ball using class variables
    def bounce(self):
        self.y_delta *= -1

    # Direction change of the ball using class variables
    def paddle_bounce(self):
        self.move_speed *= 0.9
        self.x_delta *= -1

    def reset_ball(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.paddle_bounce()
