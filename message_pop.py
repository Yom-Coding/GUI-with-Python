from tkinter import *
import tkinter.messagebox as msg
root = Tk()

msg.showinfo("Alert", "Your Computer is being hacked")
msg.showwarning("Alert", "your computer is hacked")
msg.showerror("Alert", "your computer is being hacked right now")
user_response=msg.askquestion(message="Is it June right now")
print(user_response)
print(msg.askokcancel(message="Should Software Update take place"))
print(msg.askyesno(message="are you ok to print"))
print(msg.askretrycancel(message="failed"))
root.mainloop()