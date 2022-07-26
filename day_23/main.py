import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


# Screen Settings
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Objects
player = Player()
car_manager = CarManager()
score = Scoreboard()

# Key Settings
screen.listen()
screen.onkey(player.goUp, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    # Detect succesfull crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        score.increase_level()
    
        
screen.exitonclick()