from tkinter import *
import calendar
root = Tk()
root.geometry("500x500")
root.config(background="white")
root.title("Calendar")

def show():
    print("Year Has Been Shown")

    new_window = Tk()
    year = int(year_entry.get())
    new_window.title(str(year))
    specific_year = calendar.calendar(year)
    calendar_text = Text(new_window, height=450)
    calendar_text.insert(END, specific_year)
    calendar_text.pack(pady=10, padx=10)
    new_window.mainloop()


calendar_label = Label(root, text="CALENDAR", font=("Calibri", 70))
calendar_label.pack(pady=20)
year_label = Label(root, text="Enter Year")
year_label.pack(pady=20)
year_entry = Entry(root)
year_entry.pack(pady=20)
show_calendar_button = Button(root, text="Show Calendar", command=show)
show_calendar_button.pack(pady=20)
exit_button = Button(root, text="Cancel", command=exit)
exit_button.pack(pady=20)




root.mainloop()

