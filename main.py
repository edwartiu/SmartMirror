from tkinter import *
from datetime import datetime

window = Tk()
# For Ubuntu or Mac change '-fullscreen' to '-zoomed'
window.attributes('-fullscreen', True)

# Code for widgets will go under here

# Display Time
def update_time():
    now = datetime.now()
    # Change %#I to %-I when using Ubuntu or Mac system 
    formatted_time = now.strftime("%#I:%M")
    time.config(text = formatted_time)
    window.after(500, update_time)



time = Label(window, text= '')
time.pack()


update_time()
window.mainloop()