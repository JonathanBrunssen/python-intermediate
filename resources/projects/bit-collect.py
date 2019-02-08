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
