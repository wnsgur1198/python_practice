import turtle
t = turtle.Turtle()
t.shape("turtle")

## 사각형을 그리는 함수 ---------------------------
def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)

## 클릭하는 곳에 사각형 그리는 함수 --------------
def drawit(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.color("green")
    square(50)
    t.end_fill()

# s = turtle.Screen()
# s.onscreenclick(drawit)  # 마우스 클릭 이벤트 처리 함수 등록
# s.mainloop()  # 이 코드를 추가해야 터틀 그래픽 창이 바로 안 닫힘


## 마우스로 그림그리는 콜백함수 ------------------
def draw(x, y):    
    t.goto(x,y)

# t = turtle.Turtle()
# t.shape("turtle")
# t.pensize(10)
# s = turtle.Screen()
# s.onscreenclick(draw)  # 마우스 클릭 이벤트 처리 함수 등록
# s.mainloop()  # 이 코드를 추가해야 터틀 그래픽 창이 바로 안 닫힘

## 나무 그리는 함수 -----------------------------
def tree(length):
    if length > 5:
        t.forward(length)
        t.right(20)
        tree(length-15)
        t.left(40)        
        tree(length-15)
        t.right(20)
        t.backward(length)

# t.left(90)
# t.color("brown")
# t.speed(1)
# tree(90)

## 막대 그리는 함수 ----------------
def drawBar(height):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(str(height), font=('Times New Roman', 16, "bold"))
    t.right(90)

    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

# data = [120,56,309,220,156,23,98]
# t.color("blue")
# t.fillcolor("red")
# t.pensize(3)
# for d in data:
#     drawBar(d)

## 미로만들고 탈출하기 ------------
def turn_left():
    t.left(10)
    t.forward(10)

def turn_right():
    t.right(10)
    t.forward(10)

def draw_maze(x,y):
    for i in range(2):
        t.penup()
        if i==1:
            t.goto(x+100, y+100)
        else:
            t.goto(x,y)
        t.pendown()
        t.forward(300)
        t.right(90)
        t.forward(300)
        t.left(90)
        t.forward(300)

s = turtle.Screen()
t.speed(0)

draw_maze(-300, 200)
s.onkey(turn_left, "Left")
s.onkey(turn_right, "Right")

t.penup()
t.goto(-300, 250)
t.speed(1)
t.pendown()
s.listen()
s.mainloop()