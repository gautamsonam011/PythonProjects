# Learn 2 lines of code for python program to shutdown and restart Laptop/Computer

from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")

def restart_time():
    os.system("shutdown /r /t 20")
    
def logout():
    os.system("shutdown -1")

def shutdown():
    os.system("shutdown /s /t 1")



root = Tk()

root.title("Shutdown App")
root.geometry("500x500")
root.config(bg="Blue")

re_button = Button(root,text="Restart",font=("Time New Roman",20,"bold"),bg="pink",relief=RAISED,cursor="plus",fg="red", command=restart)
re_button.place(x=150,y=60,height=50,width=200)

rt_button = Button(root,text="Restart Time",font=("Time New Roman",20,"bold"),bg="pink",relief=RAISED,cursor="plus",fg="red",command=restart_time)
rt_button.place(x=150,y=170,height=50,width=200)

lg_button = Button(root,text="Log-Out",font=("Time New Roman",20,"bold"),bg="pink",relief=RAISED,cursor="plus",fg="red",command=logout)
lg_button.place(x=150,y=270,height=50,width=200)

sh_button = Button(root,text="Shutdown",font=("Time New Roman",20,"bold"),bg="pink",relief=RAISED,cursor="plus",fg="red",command=shutdown)
sh_button.place(x=150,y=370,height=50,width=200)

root.mainloop()