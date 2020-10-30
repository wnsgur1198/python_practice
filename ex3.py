# 거북이, 토끼 경주 게임
import turtle
import random

# 외부 이미지 사용하기 ---------
screen = turtle.Screen()
image1 = "rabbit.gif"
image2 = "turtle.gif"
screen.addshape(image1)
screen.addshape(image2)

t1 = turtle.Turtle()
t1.shape(image1)
t2 = turtle.Turtle()
t2.shape(image2)

# 거북이 색상 및 모양 설정 -----------
# t1.color("pink")
# t1.shape("turtle")
t1.shapesize(5)
t1.pensize(5)

# t2.color("blue")
# t2.shape("turtle")
t2.shapesize(5)
t2.pensize(5)

# 출발점에 세우기 -----------
t1.penup()
t1.goto(-300, 0)
t2.penup()
t2.goto(-300, -200)

t1.pendown()
t2.pendown()
t1.speed(1)
t2.speed(1)

# 랜덤 이동, 100번 반복
for i in range(100):
    d1 = random.randint(1,60)
    t1.forward(d1)
    d2 = random.randint(1,60)
    t2.forward(d2)