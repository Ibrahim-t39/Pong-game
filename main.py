from turtle import Screen, Turtle
from paddle import Paddle
from score import Scoreboard
from ball import Ball
from boundary import Boundary
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
board = Scoreboard()
boundary = Boundary()
  
screen.listen()
screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)
screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)


game_is_on = True
while game_is_on:
    time.sleep(ball.pace)
    screen.update()
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
        
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.rebound()
    
    if ball.xcor() > 400:
        ball.reset_position()
        board.l_point()
        
    if ball.xcor() < -400:
        ball.reset_position()
        board.r_point()
    


        









screen.exitonclick()