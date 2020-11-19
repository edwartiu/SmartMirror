from googlecalendar import *
from weather import *
from tkinter import *
from datetime import datetime
from PIL import Image, ImageTk
import requests
from io import BytesIO
import urllib.request



URL = 'http://openweathermap.org/img/wn/10d@2x.png'

with urllib.request.urlopen(URL) as url:
    with open('temp.png', 'wb') as f:
        f.write(url.read())


image = Image.open('temp.png')



window = Tk()

img = ImageTk.PhotoImage(image)

try:
    window.attributes('-fullscreen', True)
except:
    window.attributes('-zoomed', True)
window.configure(background='black')

# Frames
header = Frame(window, bg='black')
header.pack(side=TOP, fill=X)

time_date = Frame(header, bg='black')
time_date.pack(side=LEFT)

weather = Frame(header, bg='black')
weather.pack(side=RIGHT)

todays_events = Frame(window, bg='black')
todays_events.pack(side=BOTTOM, anchor=W)

# Header widgets


# Code for widgets will go under here

time = Label(time_date, text= '', bg='black', fg='white', font=("Courier", 44))
time.grid(column=0, row=0, sticky=W)

date = Label(time_date, text= '', bg='black', fg='white', font=("Courier", 30))
date.grid(column=0,row=1, sticky=W)

weather_icon = Label(weather, image=img, bg='black')
weather_icon.grid(column=0, row = 0, rowspan=2)

temp = Label(weather, text='', bg='black', fg='white', font=("Courier", 30))
temp.grid(column=1,row=0, sticky=SW)

city = Label(weather, text='', bg='black', fg='white', font=("Courier", 30))
city.grid(column=1,row=1, sticky=NW)




todays_events_label = Label(window, text='Today\'s Events', bg='black', fg='white', font=("Courier", 30))
todays_events_label.pack(side=BOTTOM, anchor=W)





# Display Time
def update_time():
    now = datetime.now()
    try: 
        formatted_time = now.strftime("%#I:%M %p")
    except:
        formatted_time = now.strftime("%-I:%M %p")
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
        event = Label(todays_events, text = '', bg='black', fg='white', font=("Courier", 44))
        event.grid(column=0, row=4)
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


def update_weather():
    weather = get_weather()
    updated_icon = weather['icon']
    updated_temp = weather['temp']
    updated_city = weather['city']

    #weather_icon.configure(image='weather_icons/'+updated_icon)
    temp.configure(text=str(updated_temp) + u'\N{DEGREE SIGN}' )
    city.configure(text=updated_city)
    window.after(500, update_weather)






# Exit tkinter
def exit(event):
    window.destroy()

window.bind("<Escape>", exit)
update_time()
update_date()
update_todays_events()
update_weather()
window.mainloop()
