import turtle

turtle.shape("circle")
turtle.shapesize(.1,.1,5)
speed=5
x, y = 0, 0
turtle.speed(0)
xmaxsize=512
ymaxsize=256

turtle.setup(xmaxsize*2, ymaxsize*2)
xdir, ydir = speed, speed
xlimit, ylimit = xmaxsize, ymaxsize
turtle.penup()

while True:
    x = x + xdir
    y = y + ydir

    if not -xlimit < x < xlimit:
        xdir = -xdir
    if not -ylimit < y < ylimit:
        ydir = -ydir

    turtle.goto(x, y)


