from tkinter import *
root = Tk()
root.geometry("500x500")
root.config(background="white")
root.title("login page")

def login():
    print("Login Succesful")
    label.config(text="Login Succesful")
    label.place(x=200, y=340)

user_label = Label(root, text="Username")
user_label.place(x=50, y=100)
user_entry = Entry(root)
user_entry.place(x=150, y=95)
pass_label = Label(root, text="Password")
pass_label.place(x=50,y=200)
pass_entry = Entry(root)
pass_entry.place(x=150, y=195)
login_button = Button(root, text="Login", command=login)
login_button.place(x=75, y=275)
cancel_button = Button(root, text="Cancel", command=root.destroy)
cancel_button.place(x=175, y=275)
label = Label(root)

root.mainloop()

