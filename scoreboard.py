from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()

        self.goto(0,260)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score}", move=False, align="center", font=("Arial", 18, "normal"))
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",move=False, align="center", font=("Arial", 18, "normal"))