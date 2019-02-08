# python-intermediate-plans

### Day-2: Simon Says

Today students will create their own version of the classic Hasbro game, Simon Says.

#### Hasbro's Version:

![simon-says-hasbro](https://github.com/Fun2LearnCode/python-intermediate-plans/blob/master/resources/pics/simon-says-hasbro.jpg)

#### Our Version:

![simon-says-tkinter](https://github.com/Fun2LearnCode/python-intermediate-plans/blob/master/resources/pics/simon-says-tkinter.png)

---

## Table of Contents

* [Constructor](https://github.com/Fun2LearnCode/python-intermediate-plans/tree/master/day-2#step-1)

* [Building the Board](https://github.com/Fun2LearnCode/python-intermediate-plans/tree/master/day-2#step-2)

* [On-Click method](https://github.com/Fun2LearnCode/python-intermediate-plans/tree/master/day-2#step-3)

* [Computer-Turn method](https://github.com/Fun2LearnCode/python-intermediate-plans/tree/master/day-2#step-4)

* [Flash method](https://github.com/Fun2LearnCode/python-intermediate-plans/tree/master/day-2#step-5)

* [Packing the board](https://github.com/Fun2LearnCode/python-intermediate-plans/tree/master/day-2#step-6)

* [Completed Project](https://github.com/Fun2LearnCode/python-intermediate-plans/tree/master/day-2#completed-project)

---

### Step 1

Begin by importing libraries, declaring and instantiating variables, and creating arrays for our colors and the buttons on our game board. This is our "constructor." We must import messagebox separately from the everything(*) tag because tkinter is weird.

```python

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

```

---

**[Back to the Top](https://github.com/Fun2LearnCode/python-intermediate-plans/tree/master/day-2#table-of-contents)**

---

### Step 2

Next, let's build our board of buttons, we will use a for loop to do this.

* The .pop() function gets the last/most recent thing added, in our case the last color added was yellow, so that will be the color of the first button on our screen, then green, blue, with red last.

* The "lambda" creates a temporary function within our loop.

* On_Click() is a custom method we will define in the next step.

```python

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

# new material starts here

for x in range(len(board)):
    for y in range(len(board[x])):
        b = Button(f,bg=colors.pop(),command=lambda row = x,
                   column = y:On_Click(row,column),
                   height = 16, width = 32)
        b.grid(row=x,column=y)
        board[x][y] = b

# end new material

```

---

**[Back to the Top](https://github.com/Fun2LearnCode/python-intermediate-plans/tree/master/day-2#table-of-contents)**

---

### Step 3

Here we will define the On_Click() method. This is what will happen every time the player clicks any of the buttons.

* We will define Computer_Turn() in the next step.

```python

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

# new material starts here

def On_Click(x,y):
    global computer_buttons
    global player_buttons
    for row in board:
        for button in row:
            if(button["bg"] == "white"):
                return
    if board[x][y]["bg"] != player_buttons.pop(0)["bg"]:
        messagebox.showinfo("You Lost","You lost after "+str(len(computer_buttons))+" turns.")
        computer_buttons = []
        player_buttons = []
    if len(player_buttons) == 0:
        Computer_Turn()

# end new material

for x in range(len(board)):
    for y in range(len(board[x])):
        b = Button(f,bg=colors.pop(),command=lambda row = x,
                   column = y:On_Click(row,column),
                   height = 16, width = 32)
        b.grid(row=x,column=y)
        board[x][y] = b

```

---

**[Back to the Top](https://github.com/Fun2LearnCode/python-intermediate-plans/tree/master/day-2#table-of-contents)**

---

### Step 4

Next, we have to define how the computer will tell the player which buttons to click and in which order. Here is the Computer_Turn() method.

* Flash() will be defined in the next step.

```python

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
        messagebox.showinfo("You Lost","You lost after "+str(len(computer_buttons))+" turns.")
        computer_buttons = []
        player_buttons = []
    if len(player_buttons) == 0:
        Computer_Turn()

# new material starts here

def Computer_Turn():
    global computer_buttons
    global player_buttons
    random_button = board[random.randint(0,1)][random.randint(0,1)]
    computer_buttons.append(random_button)
    for x in range(len(computer_buttons)):
        Flash(computer_buttons[x],x)
    player_buttons = list(computer_buttons)

# end new material

for x in range(len(board)):
    for y in range(len(board[x])):
        b = Button(f,bg=colors.pop(),command=lambda row = x,
                   column = y:On_Click(row,column),
                   height = 16, width = 32)
        b.grid(row=x,column=y)
        board[x][y] = b


```

---

**[Back to the Top](https://github.com/Fun2LearnCode/python-intermediate-plans/tree/master/day-2#table-of-contents)**

---

### Step 5

Next, we will define what a button flash is. All we will do it make the button change from whatever color it is, to white to mimic the flashing light within the actual game.

```python

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
        messagebox.showinfo("You Lost","You lost after "+str(len(computer_buttons))+" turns.")
        computer_buttons = []
        player_buttons = []
    if len(player_buttons) == 0:
        Computer_Turn()

# new material starts here

def Flash(button, x):
    button_color = button["bg"]
    button.after(x*1000, lambda:button.config(bg="white"))
    button.after(x*1000+1000,lambda:button.config(bg=button_color))

# end new material

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

```

---

**[Back to the Top](https://github.com/Fun2LearnCode/python-intermediate-plans/tree/master/day-2#table-of-contents)**

---

### Step 6

Finally we must pack everything into the frame and tell the game when to call the computer's turn.

```python

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
        messagebox.showinfo("You Lost","You lost after "+str(len(computer_buttons))+" turns.")
        computer_buttons = []
        player_buttons = []
    if len(player_buttons) == 0:
        Computer_Turn()

def Flash(button, x):
    button_color = button["bg"]
    button.after(x*1000, lambda:button.config(bg="white"))
    button.after(x*1000+1000,lambda:button.config(bg=button_color))

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

# new material starts here

Computer_Turn()
f.pack()
mainloop()

# end new material

```

---

**[Back to the Top](https://github.com/Fun2LearnCode/python-intermediate-plans/tree/master/day-2#table-of-contents)**

---

### [Completed Project](https://github.com/Fun2LearnCode/python-intermediate-plans/blob/master/resources/projects/simon-says.py)

```python

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
        messagebox.showinfo("You Lost","You lost after "+str(len(computer_buttons))+" turns.")
        computer_buttons = []
        player_buttons = []
    if len(player_buttons) == 0:
        Computer_Turn()

def Flash(button, x):
    button_color = button["bg"]
    button.after(x*1000, lambda:button.config(bg="white"))
    button.after(x*1000+1000,lambda:button.config(bg=button_color))

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

```

---

**[Back to the Top](https://github.com/Fun2LearnCode/python-intermediate-plans/tree/master/day-2)**

---