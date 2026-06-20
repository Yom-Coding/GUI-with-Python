from tkinter import *
import tkinter.font as f
root = Tk()
root.geometry("600x300")
root.config(background="white")

def convert():
    kg_value =kg.get()
    if kg_value.replace(".", "", 1).isdigit():
        kg_value = float(kg_value) 
        gram_value = round(kg_value*1000, 2)
        pound_value = round(kg_value*2.20462, 2)
        ounce_value = round(kg_value*35.274, 2)
        grams.config(text=gram_value)
        ounce.config(text=ounce_value)
        pounds.config(text=pound_value)
        error_label.grid_forget()
    else:
        error_label.grid(row=2, column=0, columnspan=3)


font_for_text = f.Font(family="Calibri" , size= 25, weight= "bold")


topframe= Frame(root)
topframe.pack()
kg_label = Label(topframe, text= "Enter The Weight In KG", font= font_for_text)
kg_label.grid(row=0, column=0)
kg = Entry(topframe)
kg.grid(row=0, column=1)
convert = Button(topframe, text= "Convert", command=convert, font = font_for_text) 
convert.grid(row=1, column=0, columnspan=2)
bottomframe = Frame(root)
bottomframe.pack()
grams_label = Label(bottomframe, text="Grams", font= font_for_text)
grams_label.grid(row=0, column=0)
pounds_label = Label(bottomframe, text="Pounds", font = font_for_text)
pounds_label.grid(row=0, column=1)
ounce_label = Label(bottomframe, text="Ounce", font = font_for_text)
ounce_label.grid(row=0, column=2)
grams = Label(bottomframe)
grams.grid(row=1, column=0)
pounds = Label(bottomframe)
pounds.grid(row=1, column=1)
ounce = Label(bottomframe)
ounce.grid(row=1, column=2)
error_label = Label(bottomframe, text="This is not a suitable number, please try again", font = font_for_text)








root.mainloop()