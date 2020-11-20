# 공 맞추기 게임
from ex33 import *

class BallGame(Ball):
    def move(self):
        self.canvas.move(self.id,self.xspeed,self.yspeed)
        (x1,y1,x2,y2)=self.canvas.coords(self.id)
        (self.x,self.y)=(x1,y1)
        if x1<=0 or x2>=WIDTH:
            self.xspeed*=-1
        if y1<=0 or y2>=HEIGHT:
            self.yspeed*=-1
    def setSpeed(self, speed):
        self.xspeed=speed

def fire(event):       
    bullet.setSpeed(10)

bullet=BallGame(canvas,"blue",10,100,200,0,0) 
target=BallGame(canvas,"red",30,600,200,0,10)
while True:
    target.move() 
    bullet.move()   
    window.update()
    time.sleep(0.03)
    canvas.bind("<Button-1>",fire)