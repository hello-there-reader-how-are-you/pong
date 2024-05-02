#https://mcsp.wartburg.edu/zelle/python/graphics/graphics.pdf
import time
from graphics import *
import math

WIDTH = 800 
HIEGHT = 600

pane = GraphWin("pong", WIDTH, HIEGHT, autoflush=False)
pane.setBackground("white")

vid_buff = []


class bumper:
    def __init__(self, p1, p2, color="orange"):
        self.obj = Rectangle(Point(p1[0], p1[1]), Point(p2[0], p2[1]))
        self.obj.setFill(color)
        self.obj.setOutline(color)
        vid_buff.append(self)

    def draw(self):
        self.obj.undraw()
        self.obj.draw(pane)

    def move(self, speed, dir):
        print(dir)
        self.obj.undraw()
        self.obj.move(speed*math.cos(math.radians(dir)), -speed*math.sin(math.radians(dir)))
        
    def x1(self):
        return self.obj.getP1().getX()
    def y1(self):
        return self.obj.getP1().getY()
    def x2(self):
        return self.obj.getP2().getX()
    def y2(self):
        return self.obj.getP2().getY()
    

class ball:
    def __init__(self, p1, p2, color="blue"):
        self.obj = Rectangle(Point(p1[0], p1[1]), Point(p2[0], p2[1]))
        self.obj.setFill(color)
        self.obj.setOutline(color)
        vid_buff.append(self)

    speed = 0
    dir = 0

    def draw(self):
        self.obj.undraw()
        self.obj.draw(pane)

    def move(self):
        coll(self, wall)
        for i in range(self.speed):
            self.obj.undraw()
            self.obj.move(math.cos(math.radians(self.dir)), -math.sin(math.radians(self.dir)))
        
    def x1(self):
        return self.obj.getP1().getX()
    def y1(self):
        return self.obj.getP1().getY()
    def x2(self):
        return self.obj.getP2().getX()
    def y2(self):
        return self.obj.getP2().getY()


def ref():
    for i in range(len(vid_buff)):
        vid_buff[i].draw()
    update()



def coll(a, b):
    x_flag = False
    y_flag = False
    if a.x1() <= 0 or a.x2() >= WIDTH:
        x_flag = True
    if a.y1() <= 0 or a.y2() >= HIEGHT:
        y_flag = True

    A = ((b.x1() <= a.x1() <= b.x2()) and (b.y1() <= a.y1() <= b.y2()))    #a.x1(), a.y1()        
    B = ((b.x1() <= a.x2() <= b.x2()) and (b.y1() <= a.y1() <= b.y2()))    #a.x2(), a.y1()
    C = ((b.x1() <= a.x1() <= b.x2()) and (b.y1() <= a.y2() <= b.y2()))    #a.x1(), a.y2()   
    D = ((b.x1() <= a.x2() <= b.x2()) and (b.y1() <= a.y2() <= b.y2()))    #a.x2(), a.y2()

    if((A and C) or (B and D)):
        x_flag = True

    if((A and B) or (C and D)):
        y_flag = True


    if x_flag:
        a.dir = 180 - a.dir
    if y_flag:
        a.dir = 360 - a.dir


#wall = bumper((700, 0), (800, 600))
wall = bumper((250, 275), (400, 425))

orb = ball((50, 500), (75, 525))
orb.speed = 10
orb.dir = 70
ref()

i = 0
while True:
    orb.move()
    ref()
    print(i)
    time.sleep(0.01)
    i += 1






#print(f"({pane.getMouse().getX()}, {pane.getMouse().getY()}), ({pane.getMouse().getX()}, {pane.getMouse().getY()})")


pane.getMouse()
pane.close()
