from tkinter import *
root = Tk()
root.geometry("500x500")
root.config(background="blue")
root.title("window")   
button = Button(root,text="close", background="white", command=root.destroy)
button.pack(side=BOTTOM)
root.mainloop()