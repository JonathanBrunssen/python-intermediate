from tkinter import *
import random
root = Tk()
f = Frame(root, height=200, width=200)
mine_amount = 0
defuse_amount = 0
board = [[0 for x in range(30)]for y in range(20)]
board_data = [[0 for x in range(30)]for y in range(20)]

def For_Each(array, x,y,behaviour):
    for foo in range(-1, 2):
        for bar in range(-1, 2):
            if(x + foo >= 0 and y + bar >= 0):
                try:
                    behaviour(x+foo,y+bar)
                except IndexError:
                    break
def On_Click(x,y):
    global root
    if(board[x][y]['bg'] == 'blue'):
        return
    board[x][y].config(bg='green')
    if(board_data[x][y] == -1):
        board[x][y].config(bg='red')
        print("you hit a mine!")
        root.destroy()
    elif(board_data[x][y] == 0):
        For_Each(board_data,x,y, lambda a,s: On_Click(a, s) if (board[a][s]['bg'] != 'green') else "false")
    else:
        board[x][y].config(text=board_data[x][y])
        
def On_Right_Click(e,x,y):
    global root 
    global defuse_amount
    global mine_amount
    if(board[x][y]["bg"] == 'SystemButtonFace' and defuse_amount < mine_amount):
        if(board_data[x][y] == -1):
            board[x][y].config(bg='yellow')
            mine_amount -= 1
            if(mine_amount == 0):
                print("You win!")
                root.destroy()
        else:
            board[x][y].config(bg='blue')
            defuse_amount += 1
    elif(board[x][y]["bg"] == 'blue'):
        board[x][y].config(bg='SystemButtonFace')
        defuse_amount -= 1
        
for x in range(len(board)):
    for y in range(len(board[x])):
        b = Button(f,command=lambda row=x,column=y:On_Click(row,column), height=1, width=2)
        b.grid(row=x, column=y)
        b.bind("<Button-3>", lambda e, row=x, column=y:On_Right_Click(e, row,column))
        board[x][y] = b
        
for x in range(100):
    row = random.randint(0,19)
    column = random.randint(0,29)
    if(board_data[row][column] != -1):
        mine_amount = mine_amount + 1
    board_data[row][column] = -1
    
for row in range(len(board)):
    for column in range(len(board[row])):
        if(board_data[row][column] == -1):
            for foo in range(-1, 2):
                for bar in range(-1, 2):
                    if(row + foo >= 0 and column + bar >= 0 ):
                        try:
                            if(board_data[row + foo][column + bar] != -1):
                                board_data[row + foo][column + bar] += 1
                        except IndexError:
                            break
f.pack()
mainloop()
