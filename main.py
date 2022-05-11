from tkinter import *
from time import *


def update():
    time_string = strftime("%H:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%d %B %Y")
    date_label.config(text=date_string)

    window.after(1000, update)


window = Tk(className='Python clock program')

window.configure(bg='black')

time_label = Label(window, font=("Arial", 50), fg="#00FF00", bg="black")
time_label.pack()

date_label = Label(window, font=("Arial", 30), fg="#00FF00", bg="black")
date_label.pack()

day_label = Label(window, font=("Arial", 25), fg="#00FF00", bg="black")
day_label.pack()

update()

window.mainloop()
