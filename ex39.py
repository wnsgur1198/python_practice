# 키보드 이벤트 처리
from tkinter import *
from tkinter import messagebox

def keyEvent(event):
    messagebox.showinfo('키보드 이벤트','눌린키: '+chr(event.keycode))

window=Tk()
window.geometry('400x400')
window.bind('<Key>',keyEvent)

window.mainloop()