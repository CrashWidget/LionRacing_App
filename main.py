# import window stuff
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


# import iracing stuff
import irsdk

# import math stuff
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
import numpy as np


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
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # now setup basic styling of app
        self.style = ttk.Style()
        self.style.configure("BW.TLabel", foreground="black", background="white")

        # config the root window
        self.title('Lion Sandwhich Racing APP V1.0')
        self.geometry('800x600')

        # Label attribute
        self.label = ttk.Label(text='Test', style="BW.TLabel")  # create label with ttk module
        self.label.pack()

        # create a basic button
        self.button = ttk.Button(self, text='Start Iracing Connection')
        self.button['command'] = self.button_clicked  # call button clicked function
        self.button.pack()

    def button_clicked(self):
        showinfo(title='Information', message="Hello, TKinter!")


class IR(irsdk.IRSDK):
    def __init__(self):
        super().__init__()  # inherit all methods and attributes of IRSDK


# lets start up an iracing service reader
IR = IR()
IR.startup()

if __name__ == '__main__':
    # create a master window instance of tk
    app = App()  # this calls intiation function of App Class

    # start software
    app.mainloop()

    # messing around with trying to plot something to the window
    x = np.linspace(-1, 2, 50)
    y = 4 ** x + 10

    # plot = Plot(x, y, "test X", "test Y", "Lion Racing APP Test")
