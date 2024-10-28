from turtle import Turtle, Screen
FONT = ("Courier", 14, "normal")
POSITION = (-280, 265)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setposition(POSITION)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="left", font=FONT)
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align="center", font=FONT)
