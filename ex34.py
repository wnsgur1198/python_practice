# 움직이는 공을 여러 개 만들고 움직이기
from ex33 import *
import random

color_list=['yellow','green','blue','red','orange','pink','grey','black']
balls_list=[]

for i in range(10):
    color=random.choice(color_list)
    size=random.randrange(10,100)
    xspeed=random.randrange(1,10)
    yspeed=random.randrange(1,10)
    balls_list.append(Ball(canvas,color,size,0,0,xspeed,yspeed))

while True:
    for ball in balls_list:
        ball.move()
    window.update()
    time.sleep(0.03)
    