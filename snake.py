from turtle import Turtle
starting_pos = [(0, 0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for i in range(0, 3):
            self.create_segment(starting_pos[i])

    def create_segment(self,position):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.segments.append(t)

    def extend(self):
        self.create_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            newx = self.segments[i - 1].xcor()
            newy = self.segments[i - 1].ycor()
            self.segments[i].goto(newx, newy)
        self.segments[0].forward(20)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading()!=90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() !=0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)



