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


def update_todays_events():
    events = get_todays_events()
    items = len(events)
    if items == 0:
        todays_event = Label(window, text = '', bg='black', fg='white', font=("Courier", 44))
        todays_event.grid(column=0, row=4)
    elif items == 1:
        todays_event_title = events[0]['title']
        todays_event_start = events[0]['start']
        todays_event_end = events[0]['end']
        title = Label(window, text=todays_event_title,  bg='black', fg='white', font=("Courier", 44))
        title.grid(column=0, row=4)
        event_time = Label(window, text=todays_event_start+' - '+todays_event_end, bg='black', fg='white', font=("Courier", 33))
        event_time.grid(column=0, row=5)
    else:
        counter = 0
        for event in events:
            todays_event_title = event['title']
            todays_event_start = event['start']
            todays_event_end = event['end']
            title = Label(window, text=todays_event_title,  bg='black', fg='white', font=("Courier", 44))
            title.grid(column=0, row = 4+(2*counter))
            event_time = Label(window, text=todays_event_start+' - '+todays_event_end, bg='black', fg='white', font=("Courier", 33))
            event_time.grid(column=0, row=5+(2*counter))
            counter += 1
    window.after(500, update_todays_events)



time = Label(window, text= '', bg='black', fg='white', font=("Courier", 44))
time.grid(column=0, row=1)

date = Label(window, text= '', bg='black', fg='white', font=("Courier", 30))
date.grid(column=0, row=2)

todays_events_label = Label(window, text='Today\'s events', bg='black', fg='white', font=("Courier", 30))
todays_events_label.grid(column= 0, row= 3)





# Exit tkinter
def exit(event):
    window.destroy()

window.bind("<Escape>", exit)
update_time()
update_date()
update_todays_events()
window.mainloop()

print(get_todays_events())