from turtle import Turtle, Screen
import random

flag = False
screen = Screen()
screen.setup(width=1000, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Enter a color from VIBGYOR").lower()
colors = ["violet", "blue", 'indigo', 'green', 'yellow', 'orange', 'red']
y_positions = [0, 40, 80, 120, -40, -80, -120]
i = 0
turtles = []
for color in colors:
    turtle = Turtle("turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=-475, y=y_positions[i])
    i += 1
    turtles.append(turtle)

if user_bet is not None:
    flag = True


def start_race(turtle_to_move, move):
    turtle_to_move.forward(move)


winner_color = ""
while flag:
    for turtle in turtles:
        start_race(turtle, random.randint(10, 30))
        if turtle.xcor() >= 470:
            flag = False
            winner_color = turtle.getturtle().color()
if winner_color[0] == user_bet:
    print("You have WON!!")
else:
    print(f"You lost!\nThe turtle that won is {winner_color[0]}")
screen.exitonclick()
