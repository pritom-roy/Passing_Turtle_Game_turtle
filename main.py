import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()

screen.title("Help the baby turtle to pass the crowd")
screen.setup(width=600, height=600)
screen.tracer(0)

car = []
new_player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(new_player.move_turtle, "Up")

# if new_player.ycor() == 300:
#     new_player.move_reset()

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    # new_player.move_turtle()
    if new_player.ycor() == 300:
        score.increment()
        cars.speed_increase()
        new_player.move_reset()

    cars.create()
    cars.runcar()

    for obj in cars.car:
        if new_player.distance(obj) < 20:
            score.gameover()
            game_is_on = False

    screen.update()
screen.exitonclick()
