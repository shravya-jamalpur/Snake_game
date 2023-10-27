from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.7,stretch_wid=1)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        randx=random.randint(-280,280)
        randy=random.randint(-280,280)
        self.goto(randx,randy)

