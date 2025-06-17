#use tkinter module for making GUI
import tkinter as tk
from tkinter import messagebox

#use to check after every move for a winner
def check_winner():
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], 
                  [0, 3, 6], [1, 4, 7], [2, 5, 8], 
                  [0, 4, 8], [2, 4, 6]]:
        if (buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != ""):
            for i in combo:
                buttons[i].config(bg='green')
            messagebox.showinfo("Game Over", f"{buttons[combo[0]]['text']} wins!")
            root.quit()
            return  # Stop checking further

    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Game Over", "It's a draw!")
        root.quit()

#user symbol display on that button, to achieve this, will ntake index parameter
def button_click(index):
    if buttons[index]["text"] == "":
        buttons[index].config(text=current_player)
        check_winner()
        toggle_player()


#will change current player
def toggle_player():

    #will use variable which allow modification in func
    global current_player
    current_player = "O" if current_player == "X" else "X"
    label.config(text=f"Player: {current_player}'s turn")

# here will create root window using tkinter
root = tk.Tk()
root.title("Tic Tac Toe")

#here in command parameter will pass lambda func, which will call button click func
buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2, command=lambda i=i: button_click(i)) for i in range(9)]

#use enumerate fuc whic gives index along each botton, after use grid method
for i, button in enumerate(buttons):
    button.grid(row=i//3, column=i%3)

#variable
current_player = "X"

#use label didit which tells whos turn it is
label = tk.Label(root, text=f"Player: {current_player}'s turn", font=("normal", 16))

#use grid method to place label in the window
label.grid(row=3, column=0, columnspan=3)

#in last will run window using main loop method
root.mainloop()
