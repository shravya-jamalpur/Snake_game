
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("My Snake Game")
s.tracer(0)

snake = Snake()
food=Food()
scoreboard=ScoreBoard()
s.listen()
s.onkey(snake.up,"Up")
s.onkey(snake.down,"Down")
s.onkey(snake.left,"Left")
s.onkey(snake.right,"Right")

game_on = True
while (game_on):
    s.update()
    time.sleep(0.1)
    snake.move()
    if snake.segments[0].distance(food)<15:
        scoreboard.score+=1
        scoreboard.update_score()
        snake.extend()
        food.refresh()
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_on= False
        scoreboard.game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<=10:
            scoreboard.game_over()
            game_on = False
s.exitonclick()