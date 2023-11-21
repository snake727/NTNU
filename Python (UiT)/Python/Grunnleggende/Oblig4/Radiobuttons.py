from tkinter import *

class textDemo:
    def __init__(self):
        window = Tk()
        window.title("Welcome!")

        self.colorCurrent = StringVar()
        colorRed = Radiobutton(window, text="Red", variable = self.colorCurrent, value = "red", command = self.changeColor).place(x = 10, y = 10)
        colorYellow = Radiobutton(window, text="Yellow", variable = self.colorCurrent, value = "yellow", command = self.changeColor).place(x = 60, y = 10)
        colorWhite = Radiobutton(text="White")
        colorGray = Radiobutton(text="Gray")
        colorGreen = Radiobutton(text="Green")
        self.displayText = Label(window, text="Welcome!", bg = "red", height= 5, width = 25).place(x = 10, y = 80)
        moveRight = Button(text="<=")
        moveLeft = Button(text="=>")

        window.mainloop()

    def changeColor(self):
        if self.colorCurrent.get() == "red":
            self.displayText["bg"] = "red"
        elif self.colorCurrent.get() == "yellow":
            self.displayText["bg"] = "yellow"



textDemo()

