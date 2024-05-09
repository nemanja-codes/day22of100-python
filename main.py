from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()
