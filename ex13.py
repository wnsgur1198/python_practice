# 이미지 표시 프로그램
from tkinter import *

def change_img():
    path = inputBox.get()
    img = PhotoImage(file=path)
    imageLabel.configure(image=img)
    imageLabel.image = img

window = Tk()

photo = PhotoImage(file='rabbit.gif')
imageLabel = Label(window, image=photo)
imageLabel.pack()

inputBox = Entry(window)
inputBox.pack()

button = Button(window, text='Submit', command=change_img)
button.pack()

window.mainloop()