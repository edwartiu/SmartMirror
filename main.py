from googlecalendar import *
from tkinter import *
from datetime import datetime

window = Tk()
try:
    window.attributes('-fullscreen', True)
except:
    window.attributes('-zoomed', True)
window.configure(background='black')

# Code for widgets will go under here

# Display Time
def update_time():
    now = datetime.now()
    try: 
        formatted_time = now.strftime("%#I:%M")
    except:
        formatted_time = now.strftime("%-I:%M")
    time.config(text=formatted_time)
    window.after(500, update_time)

def update_date():
    now = datetime.now()
    try:
        formatted_date =  now.strftime('%A, %B %#d')
    except:
        formatted_date =  now.strftime('%A, %B %-d')
    date.config(text=formatted_date)
    window.after(500, update_date)

events = get_user_events()
print(events)




time = Label(window, text= '', bg='black', fg='white', font=("Courier", 44))
time.grid(column=0, row=1)

date = Label(window, text= '', bg='black', fg='white', font=("Courier", 30))
date.grid(column=0, row=2)







# Exit tkinter
def exit(event):
    window.destroy()

window.bind("<Escape>", exit)
update_time()
update_date()
window.mainloop()