from tkinter import *
import datetime
import time
import winsound
from threading import *
find = Tk()
find.geometry("400x400")
def Threading():
    t1=Thread(target=alarm)
    t1.start()
 
def alarm():
    while True:
        set_alarm_time = f"{hur.get()}:{min.get()}:{sec.get()}"
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time,set_alarm_time)
 
        if current_time == set_alarm_time:
            print("Good Morning !!!")
Label(find,text="Alarm Clock",font=("Helvetica 20 bold"),fg="blue").pack(pady=10)
Label(find,text="Set Time",font=("Helvetica 15 bold")).pack()
 
frame = Frame(find)
frame.pack()
 
hur = StringVar(find)
hurs = ('00', '01', '02', '03', '04', '05', '06', '07','08', '09', '10', '11', '12', '13', '14', '15','16', '17', '18', '19', '20', '21', '22', '23', '24')
hur.set(hurs[0])
 
hrs = OptionMenu(frame, hur, *hurs)
hrs.pack(side=LEFT)
 
min = StringVar(find)
mins = ('00', '01', '02', '03', '04', '05', '06', '07','08', '09', '10', '11', '12', '13', '14', '15','16', '17', '18', '19', '20', '21', '22', '23','24', '25', '26', '27', '28', '29', '30', '31','32', '33', '34', '35', '36', '37', '38', '39','40', '41', '42', '43', '44', '45', '46', '47','48', '49', '50', '51', '52', '53', '54', '55','56', '57', '58', '59', '60')
min.set(mins[0])
 
mins = OptionMenu(frame, min, *mins)
mins.pack(side=LEFT)
 
sec = StringVar(find)
secs = ('00', '01', '02', '03', '04', '05', '06', '07','08', '09', '10', '11', '12', '13', '14', '15','16', '17', '18', '19', '20', '21', '22', '23','24', '25', '26', '27', '28', '29', '30', '31','32', '33', '34', '35', '36', '37', '38', '39','40', '41', '42', '43', '44', '45', '46', '47','48', '49', '50', '51', '52', '53', '54', '55','56', '57', '58', '59', '60')
sec.set(secs[0])
 
secs = OptionMenu(frame, sec, *secs)
secs.pack(side=LEFT)
 
Button(find,text="Set Alarm",font=("Helvetica 15"),command=Threading).pack(pady=20)
find.mainloop()
