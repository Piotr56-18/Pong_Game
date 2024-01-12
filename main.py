from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

paddle_one = Paddle(350, 0)
paddle_two = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=paddle_one.move_up, key="Up")
screen.onkey(fun=paddle_one.move_down, key="Down")
screen.onkey(fun=paddle_two.move_up, key="w")
screen.onkey(fun=paddle_two.move_down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #Detect collision with paddle
    if ball.distance(paddle_one) < 50 and ball.xcor() > 320 or ball.distance(paddle_two) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    #Detect when the ball goes out of bounds
    if ball.xcor() > 380:
        ball.reset_round()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_round()
        scoreboard.r_point()
screen.exitonclick()