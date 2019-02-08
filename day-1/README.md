# python-intermediate-plans

## Day-1 : Intro to Python & Bit Collect

Today students will be introduced to python and create their own version of cookie clicker.

### Intro to python:

Go over programming basics and some mathematical concepts such as:

* modulus (denoted in python by the "%" operator)

* exponents (denoted in python by the "\*\*" operator)

* concatenation (denoted in python with the ",")

* assigning vs. boolean ("=" vs "==")

* syntax of python (explain importance of whitespace, tabbing, etc)

---

### Creating an image:

First, students must create a silly image to be used in their clicker game. Theirs doesn't have to be bitcoin related, that's just the theme for the one in this repo. We use Piskel to create our pixel art.

1. Create a drawing using piskel, make sure their canvas is 100 x 100.

2. Export their drawing as a .png, then open it up in MS Paint.

3. Scale up their image to 500 x 500 using Paint.

4. Save their image in an easy place to navigate to, usually the Camps folder.

![bit-coin](https://github.com/Fun2LearnCode/python-intermediate-plans/blob/master/resources/pics/bit-coin.png)

---

### Coding the button:

The filepath for their picture should be placed inside the quotes and the backslashes need to be changed to forward slashes.

#### Looks like this:

```python

coinLogo = PhotoImage(file="C:/filepath/image.png")

```

### [Completed Project:](https://github.com/Fun2LearnCode/python-intermediate-plans/blob/master/resources/projects/bit-collect.py)

```python

from tkinter import *
root = Tk()
root.title("Bitcollect")
coins = 0
def Btn_Press():
    def Give_Coin(label):
        global coins
        coins += 1
        label.config(text="Coins collected: "+str(coins))
    Give_Coin(label)
label = Label(root,text = "Coins collected: ", fg = "green")
label.pack()
coinLogo = PhotoImage(file="this is where the filepath for your image goes, use forward slashes")
b = Button(root, image = coinLogo,height = 500, width = 500, command = Btn_Press)
b.pack()
root.mainloop()

```

![bit-collect-tkinter](https://github.com/Fun2LearnCode/python-intermediate-plans/blob/master/resources/pics/bit-collect-tkinter.png)