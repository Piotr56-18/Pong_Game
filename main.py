from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

paddle_one = Paddle(350, 0)
paddle_two = Paddle(-350, 0)

screen.listen()
screen.onkey(fun=paddle_one.move_up, key="Up")
screen.onkey(fun=paddle_one.move_down, key="Down")
screen.onkey(fun=paddle_two.move_up, key="w")
screen.onkey(fun=paddle_two.move_down, key="s")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()