from tkinter import *
import irsdk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
import numpy as np

# lets start up an iracing service
ir = irsdk.IRSDK()
ir.startup()


class Plot:
    def __init__(self, x, y, x_label, y_label, title):
        self.x = x
        self.y = y
        self.x_label = x_label
        self.y_label = y_label
        self.title = title

        fig = plt.figure()
        plot1 = fig.add_subplot(111)
        plot1.plot(self.x, self.y)

        canvas = FigureCanvasTkAgg(fig, master=app)
        canvas.draw()
        canvas.get_tk_widget().pack()


# Frame is a class of Tkinter which is inherited into the Window class definition
# Window is now a derived class of Frame
class Window(Frame):
    # create a constructor for the main window of the program
    def __init__(self, master=None):
        # when instansilizing this class also initialize the Frame class inheritence
        Frame.__init__(self, master)  # call inherited Frame class and pass it name of master

        # create an instance variable master and assign it master
        self.master = master

        # widget can take all winddow self can access anything in the Frame class
        self.pack(fill=BOTH, expand=1)



        # create a button and link to function
        exit_button = Button(self, text="Exit", command=self.clickExitButton)

        # place button at (0,0)
        exit_button.place(x=0, y=0)

        # create some labels
        text = Label(self, text="this is just a test of label")
        text.place(x=70, y=90)

    def exitProgram(self):
        exit()

    def clickExitButton(self):
        exit()


if __name__ == '__main__':
    # create a master window
    root = Tk()

    # create variable app and assign it an instance of the object window, pass name of master window
    app = Window(root)

    # root.wm_title("LionRacing App V1.0")
    # root.minsize(200,200)
    # root.maxsize(800,800)
    # root.geometry("400x400")

    # messing around with trying to plot something to the window
    x = np.linspace(-1, 2, 50)
    y = 4 ** x + 10

    # plot = Plot(x, y, "test X", "test Y", "Lion Racing APP Test")

    root.mainloop()
