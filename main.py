import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Cross the road")
screen.tracer(0)

timy = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(timy.up, "Up")
screen.onkeypress(timy.m_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    if timy.ycor() >= 280:
        scoreboard.update_score()
        car_manager.increase()
        timy.from_start()
        timy.faster()
    for car in car_manager.all_cars:
        if car.distance(timy) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
