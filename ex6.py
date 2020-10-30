# 앵그리 터틀 게임 만들기
import turtle
import math

player = turtle.Turtle()
player.shape("turtle")
screen = player.getscreen()

def turnleft():
    player.left(5)

def turnright():
    player.right(5)

def fire():
    x = 0
    y = 0
    velocity = 50
    angle = player.heading()
    vx = velocity * math.cos(angle * 3.14 / 180.0)
    vy = velocity * math.sin(angle * 3.14 / 180.0)

    while player.ycor() >= 0:
        vx = vx
        vy -= 10
        x += vx
        y += vy
        player.goto(x, y)

# 메인
screen.onkeypress(turnleft, "Left")
screen.onkeypress(turnright, "Right")
screen.onkeypress(fire, "space")
screen.listen()

screen.mainloop()  # 이 코드를 추가해야 터틀 그래픽 창이 바로 안 닫힘