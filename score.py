from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.score = 0

    def increase_score(self):
        self.score+=1
        self.clear()
        self.goto(0,250)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Courier", 24, "normal"))