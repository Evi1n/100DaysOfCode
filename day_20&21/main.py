import turtle
import time
import random

delay = 0.10
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = r,g,b
    return color

# Screen settings
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game by Eviln")
screen.bgcolor("black")
screen.tracer(0)

first_color = random_color()

# Snake head settings
snake_head = turtle.Turtle()
snake_head.speed(0)
snake_head.shape("square")
snake_head.color("white")
snake_head.penup()
snake_head.goto(-100, -200)
snake_head.direction = 'stop'

# Food Settings
food = turtle.Turtle()
food.shape("circle")
food.penup()
food.speed(0)
food.color(first_color)

# Skor Information
skor =turtle.Turtle()
skor.speed(0)
skor.shape("square")
skor.color(first_color)
skor.penup()
skor.hideturtle()
skor.goto(0, 260)

# Move settings
def move():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        snake_head.sety(y+20)
    if snake_head.direction == "down":
        y = snake_head.ycor()
        snake_head.sety(y-20)
    if snake_head.direction == "left":
        x = snake_head.xcor()
        snake_head.setx(x-20)
    if snake_head.direction == "right":
        x = snake_head.xcor()
        snake_head.setx(x+20)

def goUp():
    if snake_head.direction != 'down':
        snake_head.direction = 'up'

def goDown():
    if snake_head.direction != 'up':
        snake_head.direction = 'down'

def goLeft():
    if snake_head.direction != 'right':
        snake_head.direction = 'left'

def goRight():
    if snake_head.direction != 'left':
        snake_head.direction = 'right'

screen.listen()
screen.onkey(goUp, "Up")
screen.onkey(goDown, "Down")
screen.onkey(goLeft, "Left")
screen.onkey(goRight, "Right")

segments = []
is_game_on = True
skor_game = 0
skor.write("Skor: {}".format(skor_game), align="center", font=("Courier", 24, "normal"))

# Game
while is_game_on:
    
    screen.update()
    x_snake = snake_head.xcor()
    y_snake = snake_head.ycor()

    if x_snake > 280  or x_snake < -280 or y_snake > 280 or y_snake < -280:
        time.sleep(1)
        snake_head.goto(0,0)
        snake_head.direction = "stop"

        for seg in segments:
            seg.goto(1000, 1000)
        segments = []
        skor.clear()
        skor.write("Skor: {}".format(skor_game), align="center", font=("Courier", 24, "normal"))
        is_game_on = False

    if snake_head.distance(food) < 17:
        var_color = first_color
        first_color = random_color()
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color(var_color)
        new_segment.penup()
        segments.append(new_segment)
        skor_game += 10
        food.color(first_color)
        x_food = random.randint(-280, 280)
        y_food = random.randint(-280, 280)
        food.goto(x_food, y_food)
        skor.clear()
        skor.write("Skor: {}".format(skor_game), align="center", font=("Courier", 24, "normal"))
        skor.color(first_color)
        delay -=0.01

    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
        
    if len(segments) > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        segments[0].goto(x, y)

    move()

    for segment in segments:
        if segment.distance(snake_head) < 18:
            time.sleep(1)
            snake_head.goto(0,0)
            snake_head.direction = "stop"
            for segment in segments:
                segment.goto(1000,1000)
            segments = []
            skor_game = 0
            skor.clear()
            skor.write("Skor: {}".format(skor_game), align="center", font=("Courier", 24, "normal"))
            is_game_on = False

    time.sleep(delay)


screen.mainloop()


