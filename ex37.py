# 지정된 위젯을 클릭했을 때 함수 호출
from tkinter import *
from tkinter import messagebox

def clickImage(event):
    messagebox.showinfo('마우스','토끼에서 마우스가 클릭됨')

window=Tk()
window.geometry('400x400')

photo=PhotoImage(file='C:/kjh-dev/kjh-python/파이썬 수업/rabbit.gif')
pLabel=Label(window,image=photo)
pLabel.bind('<Button>',clickImage)
pLabel.pack(expand=1,anchor=CENTER)

window.mainloop()