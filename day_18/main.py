import turtle
import random

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = r,g,b
    return color

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=432, height=768)

dots = turtle.Turtle()
dots.hideturtle()
dots.speed("fast")
dots.penup()
dots.setheading(225)
dots.forward(250)
dots.setheading(0)
number_of_dots = 110

def draw():

    for _ in range(1, number_of_dots+1):
        dots.color(random_color())
        dots.dot(20)
        dots.forward(40)

        if _ % 10 == 0:
            dots.setheading(90)
            dots.forward(40)
            dots.setheading(180)
            dots.forward(400)
            dots.setheading(0)   
draw()
      
screen.exitonclick()