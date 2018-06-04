############################
#         P O N G          #
# Author: Jorge Macias     #
############################

from turtle import Turtle
from random import randint

class Paddle(Turtle):
    def __init__(self,side):
        Turtle.__init__(self)
        self._xmaxsize = 512
        self._ymaxsize = 256
        self.hideturtle()
        self.penup()
        self._x = self._xmaxsize - 15 if side=="R" else -self._xmaxsize+5
        self._y= self._ymaxsize/2
        self.goto(self._x , self._y)
        self.shape("square")
        self.shapesize(3,.5,5)
        self.speed(0)
        self._speed = 20
        self.showturtle()
    def moveUp(self):
        self._y = self._y + self._speed
        self.goto(self._x, self._y)
    def moveDown(self):
        self._y = self._y - self._speed
        self.goto(self._x, self._y)

class Ball(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self._xmaxsize = 512
        self._ymaxsize = 256
        self.screen.setup(self._xmaxsize * 2, self._ymaxsize * 2)
        self.hideturtle()
        self.penup()
        self._x, self._y = randint(-self._xmaxsize, self._xmaxsize), randint(-self._ymaxsize, self._ymaxsize)
        self.goto(self._x, self._y)
        self.shape("circle")
        self.shapesize(.1,.1,5)
        self.speed(0)
        self._speed = 3
        self._xdir, self._ydir = self._speed, self._speed
        self._xlimit, self._ylimit = self._xmaxsize, self._ymaxsize
        self.showturtle()
        self.screen.onkey(self.moveRightPaddleUp,"Up")
        self.screen.onkey(self.moveRightPaddleDown,"Down")
        self.screen.onkey(self.moveLeftPaddleUp,"q")
        self.screen.onkey(self.moveLeftPaddleDown,"a")
        self.screen.listen()
        self.rightPaddle=Paddle("R")
        self.leftPaddle =Paddle("L")
    def moveRightPaddleUp(self):
        self.rightPaddle.moveUp()
    def moveRightPaddleDown(self):
        self.rightPaddle.moveDown()
    def moveLeftPaddleUp(self):
        self.leftPaddle.moveUp()
    def moveLeftPaddleDown(self):
        self.leftPaddle.moveDown()
    def move(self):
        self._x = self._x + self._xdir
        self._y = self._y + self._ydir
        if not -self._xlimit < self._x < self._xlimit:
            self._xdir = -self._xdir
        if not -self._ylimit < self._y < self._ylimit:
            self._ydir = -self._ydir
        self.goto(self._x, self._y)

ball=Ball()
while True:
    ball.move()

