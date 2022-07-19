import turtle
import random

""" DRAW A SQUARE

square = Turtle()

square.pensize(3)
for i in range(4):
    square.forward(100)
    square.left(90)
"""


""" DRAW A DASHED LINE

dashed_line = Turtle()
dashed_line.pensize(2)

for i in range(10):
    dashed_line.forward(10)
    dashed_line.penup()
    dashed_line.forward(10)
    dashed_line.pendown()
"""


""" DRAW A SHAPES

shapes = Turtle()

shapes.pensize(2)
shapes.pencolor("blue")

def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        shapes.forward(100)
        shapes.right(angle)

for i in range(3, 11):
    draw_shape(i)
    
shapes.exitonclick()
"""


""" MY CODE FOR RANDOM WALK

def go_right(walker, step):
    walker.forward(step)
    
def go_up(walker, step):
    walker.left(90)
    walker.forward(step)
    
def go_left(walker, step):
    walker.backward(step)

def go_down(walker, step):
    walker.right(90)
    walker.forward(step)
            
def make_random_walk(step_number, step_size):
    random_walk = turtle.Turtle()
    random_walk.pensize(3)
    
    colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
    move_dict = {1: go_up,
                 2: go_right,
                 3: go_left,
                 4: go_down
                 }
    for _ in range(step_number):
        walker = move_dict[random.randint(1, 4)]
        random_walk.color(random.choice(colours))
        walker(random_walk, step_size)
         
w = turtle.Screen()
w.setup(width=432,height=768)
make_random_walk(100, 30)
w.exitonclick()
""" 

""" MY CODE 2 FOR RANDOM WALK

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = r,g,b
    return color

def random_walk():
    walk = turtle.Turtle()
    walk.pensize(6)
    walk.hideturtle()

    directions = [0, 90, 180, 270]

    for _ in range(100):
        walk.setheading(random.choice(directions))
        walk.pencolor(random_color())
        walk.forward(20)

w = turtle.Screen()
w.setup(width=432,height=768)
w.bgcolor("black")
random_walk()
w.exitonclick()

"""

"""DRAW A SPIROGRAPH (CIRCLE)
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = r,g,b
    return color

def spirograph():
    draw = turtle.Turtle()
    draw.hideturtle()
    draw.speed("fastest")

    for _ in range(100):
        draw.color(random_color())
        draw.circle(100)
        draw.left(10)


w = turtle.Screen()
w.setup(width=432,height=768)
w.bgcolor("black")
spirograph()
w.exitonclick()
"""


"""MY SPIROGRAPH CODE 2 (SQUARE)"""
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = r,g,b
    return color

def draw_square(square):
    
    for i in range(4):
        square.forward(150)
        square.left(90)


def spirograph():
    draw = turtle.Turtle()
    draw.hideturtle()
    draw.speed("fastest")
   
    for _ in range(100):
        draw.color(random_color())
        draw_square(draw)
        draw.left(10)

w = turtle.Screen()
w.setup(width=432,height=768)
w.bgcolor("black")
spirograph()
w.exitonclick()