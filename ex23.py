# 메모장 만들기
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

def open():
    file=filedialog.askopenfile(parent=window,mode='r')
    if file!=None:
        lines=file.read()
        text.insert('1.0',lines)
        file.close()

def save():
    file=filedialog.asksaveasfile(parent=window,mode='w')
    if file!=None:
        lines=text.get('1.0',END+'-1c')
        file.write(lines)
        file.close()

def exit():
    if messagebox.askokcancel("Quit","종료하시겠습니까?"):
        window.destroy()

def about():
    label=messagebox.showinfo("About","메모장 프로그램")

# 윈도우 창 생성
window=Tk()
text=Text(window,height=30,width=80)
text.pack()

# 메뉴 생성
menu=Menu(window)
window.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label='파일',menu=filemenu)
filemenu.add_command(label='열기',command=open)
filemenu.add_command(label='저장',command=save)
filemenu.add_command(label='종료',command=exit)
helpmenu=Menu(menu)
menu.add_cascade(label='도움말',menu=helpmenu)
helpmenu.add_command(label='프로그램 정보',command=about)

window.mainloop()