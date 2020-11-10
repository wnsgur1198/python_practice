# 터틀 상속 - 색깔바꾸기
from turtle import *

class MyTurtle(Turtle):
    def glow(self,x,y):
        self.fillcolor('red')

turtle=MyTurtle()
turtle.shape('turtle')
turtle.onclick(turtle.glow)

screen = turtle.getscreen()
screen.mainloop()           # 이 코드를 추가해야 터틀 그래픽 창이 바로 안 닫힘