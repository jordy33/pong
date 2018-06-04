############################
#         P O N G          #
# Author: Jorge Macias     #
############################
from turtle import Turtle
from random import randint

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
        self._speed = 5
        self._xdir, self._ydir = self._speed, self._speed
        self._xlimit, self._ylimit = self._xmaxsize, self._ymaxsize
        self.showturtle()
    def move(self):
        self._x = self._x + self._xdir
        self._y = self._y + self._ydir
        if not -self._xlimit < self._x < self._xlimit:
            self._xdir = -self._xdir
        if not -self._ylimit < self._y < self._ylimit:
            self._ydir = -self._ydir
        self.goto(self._x, self._y)

balls=1
objs=[Ball() for item in range(balls)]
while True:
    for item in range(balls):
        objs[item].move()


