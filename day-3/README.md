# python-intermediate-plans

## Day-3: Tic-Tac-Toe

Today students will create their own version of noughts and crosses, better known in the U.S. as Tic-Tac-Toe.

---

![tic-tac-toe-tkinter](https://github.com/Fun2LearnCode/python-intermediate-plans/blob/master/resources/pics/tic-tac-toe-tkinter.png)

---

### Table of Contents

* [Constructor](https://github.com/Fun2LearnCode/python-intermediate-plans/tree/master/day-3#step-1)

* [Building the Board](https://github.com/Fun2LearnCode/python-intermediate-plans/tree/master/day-3#step-2)

* [On-Click method](https://github.com/Fun2LearnCode/python-intermediate-plans/tree/master/day-3#step-3)

* [Check-Winner method](https://github.com/Fun2LearnCode/python-intermediate-plans/tree/master/day-3#step-4)

* [Packing the board](https://github.com/Fun2LearnCode/python-intermediate-plans/tree/master/day-3#step-5)

* [Completed Project](https://github.com/Fun2LearnCode/python-intermediate-plans/tree/master/day-3#completed-project)

---

#### Step 1

First, we must import our tkinter libraries, along with messagebox, like before. Then, we will create all our variables and arrays.

```python

from tkinter import *
from tkinter import messagebox
root = Tk()
f = Frame(root, height=200, width=200)
board = [[0 for x in range(3)] for y in range(3)]
turn = 1

```

---

**[Back to the Top](https://github.com/Fun2LearnCode/python-intermediate-plans/tree/master/day-3#table-of-contents)**

---

#### Step 2

Next, we will build the board. Tic\-tac\-toe is a 3x3 board, so that's what we'll create using the draw_board() method.

```python

from tkinter import *
from tkinter import messagebox
root = Tk()
f = Frame(root, height=200, width=200)
board = [[0 for x in range(3)] for y in range(3)]
turn = 1

# new material begins here

def draw_board():
    global board
    global turn
    turn = 1
    for x in range(len(board)):
        for y in range(len(board[x])):
            b = Button(f, command=lambda row=x, column=y:on_click(row, column),height=8, width=16)
            b.grid(row=x, column=y)
            board[x][y] = b

# end new material

```

---

**[Back to the Top](https://github.com/Fun2LearnCode/python-intermediate-plans/tree/master/day-3#table-of-contents)**

---

#### Step 3

Next, let's define the on_click() method so our buttons will know what to do when we click on them.

```python

from tkinter import *
from tkinter import messagebox
root = Tk()
f = Frame(root, height=200, width=200)
board = [[0 for x in range(3)] for y in range(3)]
turn = 1

# new material begins here

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

# end new material

def draw_board():
    global board
    global turn
    turn = 1
    for x in range(len(board)):
        for y in range(len(board[x])):
            b = Button(f, command=lambda row=x, column=y:on_click(row, column),height=8, width=16)
            b.grid(row=x, column=y)
            board[x][y] = b

```

---

**[Back to the Top](https://github.com/Fun2LearnCode/python-intermediate-plans/tree/master/day-3#table-of-contents)**

---

#### Step 4

Now for the largest chunk of code, we will check for the win conditions of the game.

```python

from tkinter import *
from tkinter import messagebox
root = Tk()
f = Frame(root, height=200, width=200)
board = [[0 for x in range(3)] for y in range(3)]
turn = 1

# new material starts here

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

# end new material

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

```

---

**[Back to the Top](https://github.com/Fun2LearnCode/python-intermediate-plans/tree/master/day-3#table-of-contents)**

---

#### Step 5

Finally, we will pack eveything into the board.

```python

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

# new material starts here

draw_board()
f.pack()
mainloop()

# end new material

```

---

**[Back to the Top](https://github.com/Fun2LearnCode/python-intermediate-plans/tree/master/day-3#table-of-contents)**

---

---

### [Completed Project](https://github.com/Fun2LearnCode/python-intermediate-plans/blob/master/resources/projects/tic-tac-toe.py)

```python

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

```

---

**[Back to the Top](https://github.com/Fun2LearnCode/python-intermediate-plans/tree/master/day-3)**

---