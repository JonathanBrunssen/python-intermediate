from tkinter import *
from tkinter import messagebox
import random
import time
root = Tk()
f = Frame(root, height = 200, width = 200)
computer_buttons = []
player_buttons = []
colors = ["red","blue","green","yellow"]
board = [[0 for x in range(2)] for y in range(2)]

def On_Click(x,y):
    global computer_buttons
    global player_buttons
    for row in board:
        for button in row:
            if(button["bg"] == "white"):
                return
    if board[x][y]["bg"] != player_buttons.pop(0)["bg"]:
        messagebox.showinfo("You Lost","You lost after "+str(len(computer_buttons))+" turns you did bad")
        computer_buttons = []
        player_buttons = []
    if len(player_buttons) == 0:
        Computer_Turn()
        
def Flash(button, x):
    button_color = button["bg"]
    button.after(x*1000, lambda:button.config(bg="white"))
    button.after(x*1000+1000, lambda:button.config(bg=button_color))
    
def Computer_Turn():
    global computer_buttons
    global player_buttons
    random_button = board[random.randint(0,1)][random.randint(0,1)]
    computer_buttons.append(random_button)
    for x in range(len(computer_buttons)):
        Flash(computer_buttons[x],x)
    player_buttons = list(computer_buttons)
    
for x in range(len(board)):
    for y in range(len(board[x])):
        b = Button(f,bg=colors.pop(),command=lambda row = x,
                   column = y:On_Click(row,column),
                   height = 16, width = 32)
        b.grid(row=x,column=y)
        board[x][y] = b
        
Computer_Turn()
f.pack()
mainloop()
            













