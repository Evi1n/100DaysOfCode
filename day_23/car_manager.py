from turtle import Turtle
import random
import turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

turtle.colormode(255)

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    # create random color
    def random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = r,g,b
        return color

    # create a car    
    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 3:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(self.random_color())
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    # move cars
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    # level up
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
