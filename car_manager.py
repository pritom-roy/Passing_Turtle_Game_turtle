from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car = []
        self.increase = STARTING_MOVE_DISTANCE
        self.hideturtle()

    def create(self):
        chance = random.randint(1, 4)
        if chance == 3:
            new_car = Turtle("turtle")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.turtlesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            ypos = random.randint(-200, 200)
            new_car.goto(x=310, y=ypos)
            self.car.append(new_car)

    def runcar(self):
        for obj in self.car:
            obj.fd(self.increase)

    def speed_increase(self):
        self.increase += 3
