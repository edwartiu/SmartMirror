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

time = Label(window, text= '', bg='black', fg='white', font=("Courier", 44))
time.pack(side=TOP, anchor=W)

date = Label(window, text= '', bg='black', fg='white', font=("Courier", 30))
date.pack(side= TOP, anchor=W)

todays_events = Frame(window, bg='black')
todays_events.pack(side=BOTTOM, anchor=W)


todays_events_label = Label(window, text='Today\'s Events', bg='black', fg='white', font=("Courier", 30))
todays_events_label.pack(side=BOTTOM, anchor=W)





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
        title = Label(todays_events, text=todays_event_title,  bg='black', fg='white', font=("Courier", 44))
        title.grid(column=0, row=4, sticky=W)
        event_time = Label(todays_events, text=todays_event_start+' - '+todays_event_end, bg='black', fg='white', font=("Courier", 33))
        event_time.grid(column=0, row=5, sticky=W)

    else:
        counter = 0
        for event in events:
            todays_event_title = event['title']
            todays_event_start = event['start']
            todays_event_end = event['end']
            title = Label(todays_events, text=todays_event_title,  bg='black', fg='white', font=("Courier", 44))
            title.grid(column=0, row = 0+(2*counter), sticky=W)
            event_time = Label(todays_events, text=todays_event_start+' - '+todays_event_end, bg='black', fg='white', font=("Courier", 33))
            event_time.grid(column=0, row=1+(2*counter), sticky=W)
            counter += 1
    window.after(500, update_todays_events)






# Exit tkinter
def exit(event):
    window.destroy()

window.bind("<Escape>", exit)
update_time()
update_date()
update_todays_events()
window.mainloop()
