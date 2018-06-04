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
        self._ylimit = self._ymaxsize
        self.goto(self._x , self._y)
        self.shape("square")
        self.shapesize(3,.5,5)
        self.speed(0)
        self._speed = 20
        self.showturtle()
    def moveUp(self):
        if self._y < self._ylimit:
            self._y = self._y + self._speed
            self.goto(self._x, self._y)
            return(self._y)
    def moveDown(self):
        if -self._ylimit < self._y:
            self._y = self._y - self._speed
            self.goto(self._x, self._y)
            return (self._y)
    def erasePaddle(self):
        self.hideturtle()

class Ball(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self._xmaxsize = 512
        self._ymaxsize = 256
        self.rightPaddlePosition=0
        self.leftPaddlePosition = 0
        self.screen.setup(self._xmaxsize * 2, self._ymaxsize * 2)
        self.hideturtle()
        self.penup()
        self._x, self._y = 0, randint(-self._ymaxsize, self._ymaxsize)
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
        self.rightPaddlePosition =self.rightPaddle.moveUp()

    def moveRightPaddleDown(self):
        self.rightPaddlePosition =self.rightPaddle.moveDown()

    def moveLeftPaddleUp(self):
        self.leftPaddlePosition =self.leftPaddle.moveUp()
    def moveLeftPaddleDown(self):
        self.leftPaddlePosition=self.leftPaddle.moveDown()
    def move(self):
        self._x = self._x + self._xdir
        self._y = self._y + self._ydir
        if not -self._xlimit < self._x < self._xlimit:
            self._xdir = -self._xdir
        if not -self._ylimit < self._y < self._ylimit:
            self._ydir = -self._ydir
        self.goto(self._x, self._y)
    def collide(self):
        if self._x <= -self._xlimit:
            if not self.leftPaddlePosition-30 <= self._y <= self.leftPaddlePosition+30:
                self.rightPaddle.erasePaddle()
                self.leftPaddle.erasePaddle()
                return(False)
        if self._x >= self._xlimit:
            if not self.rightPaddlePosition-30 <= self._y <= self.rightPaddlePosition+30:
                self.rightPaddle.erasePaddle()
                self.leftPaddle.erasePaddle()
                return(False)
        return (True)

score=0
while score<10:
    ball=Ball()
    while True:
        ball.move()
        if not ball.collide():
            break
    del ball
    score=score+1



