from tkinter import *
root = Tk()
root.geometry("600x300")
root.config(background="white")

topframe= Frame(root)
topframe.pack()
kg_label = Label(topframe, text= "Enter The Weight In KG")
kg_label.grid(row=0, column=0)
kg = Entry(topframe)
kg.grid(row=0, column=1)
convert = Button(topframe, text= "Convert")
convert.grid(row=1, column=0, columnspan=2)
bottomframe = Frame(root)
bottomframe.pack()
grams_label = Label(bottomframe, text="Grams")
grams_label.grid(row=0, column=0)
pounds_label = Label(bottomframe, text="Pounds")
pounds_label.grid(row=0, column=1)
ounce_label = Label(bottomframe, text="Ounce")
ounce_label.grid(row=0, column=2)
grams = Label(bottomframe)
grams.grid(row=1, column=0)
pounds = Label(bottomframe)
pounds.grid(row=1, column=1)
ounce = Label(bottomframe)
ounce.grid(row=1, column=2)








root.mainloop()