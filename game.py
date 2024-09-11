import turtle

# Set up the window
win = turtle.Screen()
win.title("Mini Ping Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)  # Stops window from updating automatically

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=6)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# Paddle movement
def paddle_right():
    x = paddle.xcor()
    if x < 340:
        x += 20
        paddle.setx(x)

def paddle_left():
    x = paddle.xcor()
    if x > -340:
        x -= 20
        paddle.setx(x)

# Keyboard bindings
win.listen()
win.onkeypress(paddle_right, "Right")
win.onkeypress(paddle_left, "Left")

# Main game loop
while True:
    win.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border collision (top)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    # Border collision (left and right)
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
    
    # Paddle collision
    if (ball.ycor() > -240 and ball.ycor() < -230) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.sety(-230)
        ball.dy *= -1
    
    # Ball goes below paddle (reset position)
    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1
