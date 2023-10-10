# How to do internet speed test using python. 
# pip install speedtest-cli 

from tkinter import *
import speedtest


def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    dow = str(round(sp.download()/(10**6),3))+"Mbps"
    up = str(round(sp.upload()/(10**6),3))+"Mbps"
    lab_dow.config(text=dow)
    lab_up.config(text=up)
    
    
    
sp = Tk()

sp.title("Internet Speed Test")
sp.geometry('500x700')
sp.config(bg="grey")

lab = Label(sp,text="Internet Speed Test",font=("Cursive",20,"bold"),fg="red")
lab.place(x=60,y=40,height=50,width=380)

lab = Label(sp,text="Download Speed",font=("Cursive",20,"bold"),fg="red")
lab.place(x=60,y=150,height=50,width=380)

lab_dow = Label(sp,text="00",font=("Cursive",20,"bold"),fg="red")
lab_dow.place(x=60,y=220,height=50,width=380)

lab = Label(sp,text="Upload Speed",font=("Cursive",20,"bold"),fg="red")
lab.place(x=60,y=290,height=50,width=380)

lab_up = Label(sp,text="00",font=("Cursive",20,"bold"),fg="red")
lab_up.place(x=60,y=360,height=50,width=380)

button = Button(sp,text="CHECK SPEED",font=("Time New Roman",20,"bold"),relief=RAISED,fg="red",command=speedcheck)
button.place(x=100,y=460,height=50,width=200)
sp.mainloop()

