# python-intermediate-plans

## Day-4: Minesweeper

Today students will begin building the classic Microsoft Windows game: Minesweeper.

---

#### Windows Minesweeper:

![minesweeper](https://github.com/Fun2LearnCode/python-intermediate-plans/blob/master/resources/pics/minesweeper.jpg)

### Our version:

![minesweeper-tkinter](https://github.com/Fun2LearnCode/python-intermediate-plans/blob/master/resources/pics/minesweeper-tkinter.png)

---

### Table of Contents

* [Constructor](https://github.com/Fun2LearnCode/python-intermediate-plans/tree/master/day-4#step-1)

* [For-Each method](https://github.com/Fun2LearnCode/python-intermediate-plans/tree/master/day-4#step-2)

* [On-Click method](https://github.com/Fun2LearnCode/python-intermediate-plans/tree/master/day-4#step-3)

* [On-Right-Click method](https://github.com/Fun2LearnCode/python-intermediate-plans/tree/master/day-4#step-4)

* [Start on Day 5 if time allows](https://github.com/Fun2LearnCode/python-intermediate-plans/tree/master/day-5)

---

#### Step 1

First, we will import all our libraries and create all our variables for our board.

```python

from tkinter import *
import random
root = Tk()
f = Frame(root, height=200, width=200)
mine_amount = 0
defuse_amount = 0
board = [[0 for x in range(30)]for y in range(20)]
board_data = [[0 for x in range(30)]for y in range(20)]

```

---

**[Back to the Top](https://github.com/Fun2LearnCode/python-intermediate-plans/tree/master/day-4#table-of-contents)**

---

#### Step 2

Now we will write the For_Each() method. This is important for reasons unknown as of the time of the writing of this description.

```python

from tkinter import *
import random
root = Tk()
f = Frame(root, height=200, width=200)
mine_amount = 0
defuse_amount = 0
board = [[0 for x in range(30)]for y in range(20)]
board_data = [[0 for x in range(30)]for y in range(20)]

# new material starts here

def For_Each(array, x,y,behaviour):
    for foo in range(-1, 2):
        for bar in range(-1, 2):
            if(x + foo >= 0 and y + bar >= 0):
                try:
                    behaviour(x+foo,y+bar)
                except IndexError:
                    break

# end new material

```

---

**[Back to the Top](https://github.com/Fun2LearnCode/python-intermediate-plans/tree/master/day-4#table-of-contents)**

---

#### Step 3

Next, we will create the On_Click() method, this will tell the game what to do when we click on a button. In the original game, this is supposed to expand the board until the edges get close to mines, which are represented in numeric form which tells the player how many bombs are located around that cell.

```python

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

# new material starts here

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

# end new material

```

---

**[Back to the Top](https://github.com/Fun2LearnCode/python-intermediate-plans/tree/master/day-4#table-of-contents)**

---

#### Step 4

Next, we will create the On_Right_Click() method, which will be used to mark where the bombs are once you figure out their positions on the board.

```python

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

# new material starts here

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

# end new material

```

---

## [Start on Day 5 if time allows](https://github.com/Fun2LearnCode/python-intermediate-plans/tree/master/day-5)