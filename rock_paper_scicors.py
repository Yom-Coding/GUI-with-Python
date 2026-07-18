from tkinter import * 
import random
root = Tk()
root.geometry("500x500")
root.config(background="white")
options = ["Rock", "Paper", "Scissors"]
player_score = 0
computer_score = 0
def game (player_input):
    global player_score, computer_score
    computer_input = random.choice(options)
    if player_input == computer_input:
        result.config(text = "It is a Tie")

    elif (player_input == "Rock" and computer_input == "Scissors") or (player_input == "Paper" and computer_input == "Rock") or (player_input == "Scissors" and computer_input == "Paper"):
        result.config(text = "You have Won")
        player_score = player_score + 1

    else:
        result.config(text = "You have Lost")
        computer_score = computer_score + 1
    
    you_selected.config(text = "You have Selected :" + player_input)
    comp_selected.config(text = "The Computer Selected :" + computer_input)

    your_score.config(text = "Your Score : " + str(player_score))
    comp_score.config(text = "Comp Score : " + str(computer_score))
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