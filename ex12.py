# 온도변환 프로그램 gui 버전
from tkinter import *

def process():
    temperature = float(e1.get())
    mytemp = (temperature-32)*5/9    
    e2.insert(0, str(mytemp))

window = Tk()

# l1 = Label(window, text="화씨")
# l2 = Label(window, text="섭씨")
l1 = Label(window, text="화씨", font='helvetica 16 italic')     # 폰트 지정
l2 = Label(window, text="섭씨", font='helvetica 16 italic')
# l1.pack()       # 압축(pack) 배치관리자 지정
# l2.pack()
l1.grid(row=0, column=0)        # 격자(grid) 배치관리자 지정
l2.grid(row=1, column=0)

e1 = Entry(window)
e2 = Entry(window)
# e1 = Entry(window, bg='yellow', fg='white')     # 배경색, 글자색 지정
# e2 = Entry(window, bg='yellow', fg='white')
# e1.pack()
# e2.pack()
e1.grid(row=0, column=1)        # 격자(grid) 배치관리자 지정
e2.grid(row=1, column=1)

b1 = Button(window, text="화씨->섭씨", command=process)     # 버튼 이벤트 지정
b2 = Button(window, text="섭씨->화씨")
# b1.pack()
# b2.pack()
b1.grid(row=2, column=0)        # 격자(grid) 배치관리자 지정
b2.grid(row=2, column=1)

window.mainloop()