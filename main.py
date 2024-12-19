from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=700,height=500)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((320,0))
l_paddle = Paddle((-320,0))

ball = Ball()
scoreboard = scoreboard()



screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 240 or ball.ycor() < -240:
        ball.bounce_y()


    #detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 300 or ball.distance(l_paddle) < 50 and ball.xcor() < -300:
        ball.bounce_x()

    #detect R paddle collision beyond wall
    if ball.xcor() > 340:
        ball.reset_position()
        scoreboard.l_point()

    #detect l paddle collsion beyond the wall
    if ball.xcor() < -340:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()