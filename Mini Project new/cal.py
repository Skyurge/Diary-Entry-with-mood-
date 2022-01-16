# Import Required Library
from tkinter import *
from tkcalendar import Calendar
import os
import config

# Create Object
root = Tk()

# Set geometry
root.geometry("400x400")

# Add Calendar
cal = Calendar(root, selectmode = 'day',year = 2020, month = 5,day = 22,date_pattern= 'dd-mm-yyyy')

cal.pack(pady = 20)

def grad_date():
        try:
                cdate = cal.get_date()
                config.date = cdate
                config.fname="svf/"+config.cuser+"-"+config.date + '.txt'
                #if(os.path.exists(config.fname)):
                from TK2.py import Window
                root=Tk()
                obj=Window(root)
                root.mainloop()
                #root.destroy()
        except Exception:
                print('Diary opened')

# Add Button and Label
Button(root, text = "Open Diary",
	command = grad_date).pack(pady = 20)

Ldate = Label(root, text = "")
Ldate.pack(pady = 20)

# Execute Tkinter
root.mainloop()
