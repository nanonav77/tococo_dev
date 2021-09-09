from tkinter import *

class FrameOrder(Tk):

    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        initframe = Frame(self, bg='#BDC3C7',width=420,height=500)
        initframe.place(x=280, y=105)   
                     

if __name__ == "__main__":
    app = FrameOrder(None)
    app.title('Initial')
    app.mainloop()