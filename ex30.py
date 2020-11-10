# 터틀 클래스 + 자동차 클래스
from turtle import *

class Car:
    def __init__(self,speed,color,model):
        self.speed=speed
        self.color=color
        self.model=model  
        self.turtle=Turtle()
        self.turtle.shape('C:\kjh-dev\kjh-python\파이썬 수업\car.gif')      

    def drive(self):
        self.turtle.forward(self.speed)
    
    def left_turn(self):
        self.turtle.left(90)

## 미리 모양을 등록해야만 쓸 수 있음. gif형식만 됨. 절대경로를 지정해줘야 함.
register_shape('C:\kjh-dev\kjh-python\파이썬 수업\car.gif')
myCar=Car(200,'silver','e-class')
for i in range(100):
    myCar.drive()
    myCar.left_turn()