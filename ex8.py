# 오륜기 그리기
import turtle

def draw_olympic_symbol():
    positions = [ [0,0,"blue"], [-120,0,"purple"], [60,60,"red"], [-60,60,"yellow"], [-180,60,"green"]]
    for x,y,c in positions:
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.color(c,c)        # 테두리색과 채우기색 지정
        t.begin_fill()
        t.circle(30)
        t.end_fill()

t = turtle.Turtle()
draw_olympic_symbol()