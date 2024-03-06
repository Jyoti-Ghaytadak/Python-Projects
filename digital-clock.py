from tkinter import*
from time import*
w=Tk()
w.title("Digital clock")
w.geometry("420x150")
w.resizable(1,1)
l=Label(w,font=("arial",68,"bold"),bg="yellow",fg="red",bd=25)
l.grid(row=0,column=1)
def update():
    t=strftime("%H:%M:%S")
    l.config(text=t)
    w.after(1000,update)
update()
w.mainloop()