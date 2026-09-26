from tkinter import *
from tkinter.messagebox import *
root = Tk() 

hours = StringVar()
minutes = StringVar()
seconds = StringVar()
hours.set(0)
minutes.set(0)
seconds.set(0)

def start_time():
    try:
        total_time = int(hours_entry.get()) * 3600 + int(min_entry.get()) * 60 + int(sec_entry.get())
        print(total_time)
    except:
        showerror(message="Enter a correct value")

hours_entry = Entry(root, textvariable = hours)
hours_entry.grid(row= 1, column= 1)

min_entry = Entry(root, textvariable = minutes)
min_entry.grid(row=1, column= 2)

sec_entry = Entry(root, textvariable = seconds)
sec_entry.grid(row= 1, column=3)

start_button = Button(root, text="Start", command = start_time)
start_button.grid(row= 2, column = 1, columnspan= 3)

root.mainloop()