from tkinter import *
root = Tk()
root.geometry("700x500")
root.config(background="white")
root.title("Celsius to Fahrenheit")

def convert():
    new_temp = int(temp_entry.get())
    fahr_temp = (new_temp*1.8) + 32
    converted_temp.config(text="The converted Temperature is " + str(fahr_temp))
    converted_temp.pack(pady=50)


title = Label(root, text="Celsius to Fahrenheit", font=("Calibri", 60),fg='black', bg='white')
title.pack(pady=20)
enter_temp_in_celsius = Label(root, text="Enter Temperature In Celsius Here: ", fg='black', bg='white')
enter_temp_in_celsius.pack(pady=0)
temp_entry = Entry(root, bg='white', fg='black')
temp_entry.pack(pady=0)
converted_temp = Label(root, font=("Calibri", 20))
convert_button = Button(root, text="Convert", width=5, height=2, fg='green', bg='white', command=convert)
convert_button.pack(pady=50)

root.mainloop()
