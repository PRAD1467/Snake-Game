from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

sc = Screen()
sc.setup(width=600, height=600)
sc.bgcolor('black')
sc.title('My Snake Game')
sc.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()

sc.listen()
sc.onkey(fun=snake.up, key='Up')
sc.onkey(fun=snake.down, key='Down')
sc.onkey(fun=snake.left, key='Left')
sc.onkey(fun=snake.right, key='Right')

# Move Snake
game_is_on = True
while game_is_on:
    sc.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

sc.exitonclick()