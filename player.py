from turtle import Turtle

STARTING_POSITION = (0, -280)
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.speed = 10
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.color("purple")
        self.setposition(STARTING_POSITION)

    def up(self):
        self.forward(self.speed)

    def m_down(self):
        self.backward(self.speed)

    def from_start(self):
        self.goto(STARTING_POSITION)

    def faster(self):
        self.speed += 2
