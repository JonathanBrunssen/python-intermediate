from tkinter import *
from tkinter import messagebox
root = Tk()
f = Frame(root, height=200, width=200)
board = [[0 for x in range(3)] for y in range(3)]
turn = 1
def check_winner():
    if(board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]):
        if(board[1][1]["text"] == "X"):
            messagebox.showinfo("Winner", "Player One is the winner")
            draw_board()
        elif(board[1][1]["text"] == "O"):
            messagebox.showinfo("Winner", "Player Two is the winner")
            draw_board()

    if(board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]):
        if(board[1][1]["text"] == "X"):
            messagebox.showinfo("Winner", "Player One is the winner")
            draw_board()
        elif(board[1][1]["text"] == "O"):
            messagebox.showinfo("Winner", "Player Two is the winner")
            draw_board()

    for x in range(len(board)):
        if(board[x][0]["text"] == board[x][1]["text"] == board[x][2]["text"]):
            if(board[x][1]["text"] == "X"):
                messagebox.showinfo("Winner", "Player One is the winner")
                draw_board()
            elif(board[x][1]["text"] == "O"):
                messagebox.showinfo("Winner", "Player Two is the winner")
                draw_board()
        if(board[0][x]["text"] == board[1][x]["text"] == board[2][x]["text"]):
            if(board[1][x]["text"] == "X"):
                messagebox.showinfo("Winner", "Player One is the winner")
                draw_board()
            elif(board[1][x]["text"] == "O"):
                messagebox.showinfo("Winner", "Player Two is the winner")
                draw_board()
def on_click(x, y):
    global turn
    if turn == 10:
        messagebox.showinfo("Draw", "Its a draw!")
        draw_board()
        return
    if board[x][y]["text"] == "":
        if(turn % 2 == 1):
            board[x][y].config(text="X")
        else:
            board[x][y].config(text="O")
        turn += 1
        check_winner()

def draw_board():
    global board
    global turn
    turn = 1
    for x in range(len(board)):
        for y in range(len(board[x])):
            b = Button(f, command=lambda row=x, column=y:on_click(row, column),height=8, width=16)
            b.grid(row=x, column=y)
            board[x][y] = b
draw_board()
f.pack()
mainloop()
