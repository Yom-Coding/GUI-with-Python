from tkinter import *
root = Tk()
root.geometry("500x500")
root.config(background="white")

def game (player_input):
    print (player_input)

topframe = Frame(root)
topframe.pack()
rpc_label = Label(topframe, text="Rock Paper Scissors Game")
rpc_label.grid(row=1, column=1, columnspan= 3)
result=Label(topframe)
result.grid(row=2, column=1, columnspan=3)
rock_button=Button(topframe, text="Rock", command= lambda: game("Rock"))
rock_button.grid(row=3, column=1)
paper_button = Button(topframe, text="Paper", command = lambda: game("Paper"))
paper_button.grid(row=3, column=2) 
scissors_button=Button(topframe, text="Scissors", command= lambda: game("Scissors"))
scissors_button.grid(row=3,column=3)
bottomframe=Frame(root)
bottomframe.pack()
your_score= Label(bottomframe, text= "Your Score: ")
your_score.grid(row=1, column=1)
comp_score= Label(bottomframe, text= "Comp Score: ")
comp_score.grid(row=2, column=1)
you_selected= Label(bottomframe, text= "You Selected: ")
you_selected.grid(row=1, column=2)
comp_selected= Label(bottomframe, text= "Comp Selected: ")
comp_selected.grid(row=2, column=2)


root.mainloop()