# Learn to make a digital clock in python. 

from tkinter import *
import datetime

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    mi = time.strftime("%M")
    sec = time.strftime("%S")
    am = time.strftime("%p")
    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    
    
    date = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%y")
    day = time.strftime("%a")
    
    lab_date.config(text=date)
    lab_mo.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)
    
    lab_hr.after(200,date_time)  #after recall program
# call Tk class 
clock = Tk()

clock.title("       *****Digital Clock***** ")
clock.geometry('1000x500')
clock.config(bg="#33ccff")

lab_hr = Label(clock, text="00",font=('Time New Roman',50,"bold"), bg="yellow", fg="red")
lab_hr.place(x =120,y= 45, height=110,width=100)

lab_min = Label(clock, text="00",font=('Time New Roman',50,"bold"), bg="yellow", fg="red")
lab_min.place(x = 340,y= 45, height=110,width=100)

lab_sec = Label(clock, text="00",font=('Time New Roman',50,"bold"), bg="yellow", fg="red")
lab_sec.place(x = 560,y= 45, height=110,width=100)

lab_am = Label(clock, text="00",font=('Time New Roman',50,"bold"), bg="yellow", fg="red")
lab_am.place(x = 780,y= 45, height=110,width=100)

lab_hr_txt = Label(clock, text="Hour",font=('Time New Roman',20,"bold"), bg="yellow", fg="red")
lab_hr_txt.place(x = 120,y= 190, height=40,width=100)

lab_min_txt = Label(clock, text="Minute",font=('Time New Roman',20,"bold"), bg="yellow", fg="red")
lab_min_txt.place(x = 340,y= 190, height=40,width=100)

lab_sec_txt = Label(clock, text="Second",font=('Time New Roman',20,"bold"), bg="yellow", fg="red")
lab_sec_txt.place(x = 560,y= 190, height=40,width=100)

lab_am_txt = Label(clock, text="AM/PM",font=('Time New Roman',20,"bold"), bg="yellow", fg="red")
lab_am_txt.place(x = 780,y= 190, height=40,width=100)

# Now Date 
lab_date = Label(clock, text="00",font=('Time New Roman',50,"bold"), bg="pink", fg="blue")
lab_date.place(x =120,y= 270, height=110,width=100)
lab_date_txt = Label(clock, text="Date",font=('Time New Roman',20,"bold"), bg="pink", fg="blue")
lab_date_txt.place(x = 120,y= 410, height=40,width=100)

lab_mo = Label(clock, text="00",font=('Time New Roman',50,"bold"), bg="pink", fg="blue")
lab_mo.place(x = 340,y= 270, height=110,width=100)
lab_mo_txt = Label(clock, text="Month",font=('Time New Roman',20,"bold"), bg="pink", fg="blue")
lab_mo_txt.place(x = 340,y= 410, height=40,width=100)

lab_year = Label(clock, text="00",font=('Time New Roman',50,"bold"), bg="pink", fg="blue")
lab_year.place(x = 560,y= 270, height=110,width=100)
lab_year_txt = Label(clock, text="Year",font=('Time New Roman',20,"bold"), bg="pink", fg="blue")
lab_year_txt.place(x = 560,y= 410, height=40,width=100)

lab_day = Label(clock, text="00",font=('Time New Roman',50,"bold"), bg="pink", fg="blue")
lab_day.place(x = 780,y= 270, height=110,width=100)
lab_day_txt = Label(clock, text="Day",font=('Time New Roman',20,"bold"), bg="pink", fg="blue")
lab_day_txt.place(x = 780,y= 410, height=40,width=100)



date_time()
# continue run
clock.mainloop()