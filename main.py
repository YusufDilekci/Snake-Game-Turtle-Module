from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard

DELAY = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)  #0 off anlamındadır.update metodu kullanılmadığı sürece ekran güncellenmez yani değişiklik etki etmez

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, 'Up')    #onkey methodunda fonksiyon () kullanılmadan çağrılır.
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(DELAY)
    snake.move()
    #Collision with food
    if snake.head.distance(food) < 15:  #distance methoduna argument olarak bir turtle instance verilebilir.
        food.refresh()
        snake.extend()
        score_board.increase_score()
        DELAY /= 1.1

    #collision tail so yourself   bug var !!!
    for segment in snake.squares[1:]: #listeyi 2.elemanından başlayarak tarayacak
        if snake.head.distance(segment) < 10:
           score_board.reset()
           snake.reset()
           DELAY = 0.1



    #collision a wall that means exceed the boundary of window
    if snake.head.xcor() < -300 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 300:
        score_board.reset()
        snake.reset()
        DELAY = 0.1
screen.exitonclick()


