# import colorgram
#
# colors_tuple = []
# colors = colorgram.extract("Damien-Hirst-Spot-Painting-685051475.gif", 25 * 8)
# for color in colors:
#     color_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
#     colors_tuple.append(color_tuple)
#
# print(colors_tuple)
import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(1400, 700)
# screen.setworldcoordinates(30, 30, 1400, 700)

turtle.colormode(255)


timmy = Turtle()
color_list = [(160, 154, 139), (132, 98, 75), (218, 221, 221), (38, 40, 49), (60, 33, 24),
              (77, 95, 130), (216, 204, 205), (135, 169, 190), (170, 150, 37), (218, 203, 129),
              (140, 178, 161), (70, 84, 59), (151, 55, 75), (214, 224, 232), (155, 21, 14),
              (160, 108, 138), (188, 186, 211), (190, 144, 152), (214, 171, 172), (84, 139, 170),
              (36, 58, 103), (193, 86, 79), (107, 62, 4), (100, 127, 160)]


def draw():
    for row in range(0, 10):
        timmy.color(random.choice(color_list))
        timmy.dot(20)
        timmy.penup()
        timmy.forward(50)


def reposition():
    timmy.penup()
    timmy.left(90)
    timmy.forward(40)
    timmy.left(90)
    timmy.forward(500)
    timmy.right(180)
    timmy.pendown()


timmy.penup()
timmy.goto(-250, -250)
timmy.shape('circle')
timmy.speed("fastest")


column = 0
while column <= 9:
    draw()
    reposition()
    column += 1

timmy.penup()
timmy.goto(-250, -250)
screen.exitonclick()
