from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = 10

    def create_car(self):
        rand_num = random.randint(1, 6)
        if rand_num == 1:
            car = Turtle(shape="square")
            car.penup()
            car.color(random.choice(COLORS))
            car.setheading(180)
            car.shapesize(1, 2)
            random_y = random.randint(-240, 240)
            car.setposition(x=300, y=random_y)
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def increase(self):
        self.car_speed += 3
