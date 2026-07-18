from tkinter import *
from time import strftime
root = Tk()
root.geometry("100x50") 
root.config(background="white")

visual_clock = Label(root)
visual_clock.pack()

def digital_time():
    t = strftime("%H:%M:%S")
    visual_clock.config(text= t)
    visual_clock.after(1000, digital_time)
digital_time()
root.mainloop()