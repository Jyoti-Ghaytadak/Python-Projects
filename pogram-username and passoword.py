from tkinter import *
def login():
    uname=username.get()
    pwd=password.get()
    if uname==""or pwd=="":
        message.set("fill the empty fild!!!")
    else:
        if uname=="abc@gmail.com"and pwd=="abc123":
         message.set("login success")
        else:
         message.set("wrong username or password!!!")
def loginform():
    global login_screen
    login_screen=Tk()
    login_screen.title("login from")
    login_screen.geometry("300x250")
    global message
    global username
    global  password
    username=StringVar()
    password=StringVar()
    message=StringVar()
    Label(login_screen,width="300",text="please enter detail below",bg="orange",fg="white").pack()
    Label(login_screen,text="").pack()
    Label(login_screen,text="enter username*").pack()
    Entry(login_screen,textvariable=username).pack()
    Label(login_screen,text="enter password*").pack()
    Entry(login_screen,textvariable=password,show="*").pack()
    Label(login_screen,text="",textvariable=message).pack()
    Button(login_screen,text="login",width=10,height=1,bg="orange",command=login).pack()
    login_screen.mainloop()
loginform()


