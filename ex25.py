# 필로우를 이용한 영상처리, 45도 회전
from PIL import Image,ImageTk
import tkinter as tk

window=tk.Tk()
canvas=tk.Canvas(window, width=500, height=500)
canvas.pack()

img=Image.open("c:\kjh-dev\kjh-python\파이썬 수업\lena.png")

# 45도 회전
out=img.rotate(45)

tk_img=ImageTk.PhotoImage(out)
canvas.create_image(250,250,image=tk_img)
window.mainloop()