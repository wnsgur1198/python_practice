import turtle

t = turtle.Turtle()
t.shape("turtle")

## n각형을 그리는 함수 ------------------------
def n_polygon(n, length):
    for _ in range(n):
        t.forward(length)
        t.left(360 // n)  # 정수 나눗셈은 //으로 함

# for _ in range(10):
#     t.left(20)
#     n_polygon(6, 100)

## 원의 넓이를 구하는 함수 ----------------------
def calculate_area(radius):
    global area                 # 전역변수에 값을 저장한다고 알림
    area = 3.14 * radius ** 2
    return

# area = 0
# r = float(input("원의 반지름: "))
# calculate_area(r)
# print(area)