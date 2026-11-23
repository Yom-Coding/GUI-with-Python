import tkinter as tk
root = tk.Tk()
root.geometry("500x500")
def tic_tac_toe(new_interface, mode):
    pass


def start_player_game(mode):
    new_interface = tk.Tk()
    new_interface.geometry("500x500")
    tic_tac_toe(new_interface, mode)

    
    
    
    
    new_interface.mainloop()



one_player_button=tk.Button(root, text= "1 Player", width= 5, height= 2, command=lambda:start_player_game("one_player"))
one_player_button.pack(pady=100)

two_player_button=tk.Button(root, text= "2 Player", width= 5, height= 2, command=lambda:start_player_game("two_player"))
two_player_button.pack(pady=25)
root.mainloop()
