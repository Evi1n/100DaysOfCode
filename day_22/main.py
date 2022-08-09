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
screen.title('Pong Game by Eviln')
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)

# Paddle Left
paddle_left = turtle.Turtle()
paddle_left.speed("fastest")
paddle_left.shape('square')
paddle_left.color('white')
paddle_left.penup()
paddle_left.goto(-350, 0)
paddle_left.shapesize(5, 1)

# Paddle Right
paddle_right = turtle.Turtle()
paddle_right.speed("fastest")
paddle_right.shape('square')
paddle_right.color('white')
paddle_right.penup()
paddle_right.goto(350, 0)
paddle_right.shapesize(5, 1)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color(random_color())
ball.penup()
ball.dx = 0.15
ball.dy = 0.15

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color(random_color())
pen.penup()
pen.goto(0, 260)
pen.write("Player Left: 0  Player Right: 0", align='center', font=('Courier', 20, 'bold'))
pen.hideturtle()

# Score
score_left = 0
score_right = 0

def paddle_left_up():
    y = paddle_left.ycor()
    y += 35
    paddle_left.sety(y)

def paddle_right_up():
    y = paddle_right.ycor()
    y += 35
    paddle_right.sety(y)

def paddle_left_down():
    y = paddle_left.ycor()
    y += -35
    paddle_left.sety(y)

def paddle_right_down():
    y = paddle_right.ycor()
    y += -35
    paddle_right.sety(y)


# Keyboard binding
screen.listen()
screen.onkeypress(paddle_left_up, 'w')
screen.onkeypress(paddle_left_down, 's')
screen.onkeypress(paddle_right_up, 'Up')
screen.onkeypress(paddle_right_down, 'Down')


is_game_on = True

# Main game loop
while is_game_on:
    screen.update()

    # Moving Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.color(random_color())
        ball.goto(0, 0)
        ball.dx *= -1
        score_left += 1
        pen.clear()
        pen.write("Player Left: {}  Player Right: {}".format(score_left, score_right), align='center', font=('Courier', 20, 'bold'))

    if ball.xcor() < -390:
        ball.color(random_color())
        ball.goto(0, 0)
        ball.dx *= -1
        score_right += 1
        pen.clear()
        pen.write("Player Left: {}  Player Right: {}".format(score_left, score_right), align='center', font=('Courier', 20, 'bold'))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_right.ycor() + 60 and ball.ycor() > paddle_right.ycor() -60):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_left.ycor() + 60 and ball.ycor() > paddle_left.ycor() -60):
        ball.setx(-340)
        ball.dx *= -1

    if score_left == 3:
        pen.clear()
        pen.write("Game over. The player on the {} won!".format("Left"), align='center', font=('Courier', 18, 'bold'))
        is_game_on = False

    if score_right == 3:
        pen.clear()
        pen.write("Game over. The player on the {} won!".format("Right"), align='center', font=('Courier', 18, 'bold'))
        is_game_on = False

screen.mainloop()