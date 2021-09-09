from tkinter import *

class FrameHistory(Tk):

    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        initframe = Frame(self, bg='#BDC3C7',width=480,height=500)
        initframe.place(x=730, y=105)   
                     

if __name__ == "__main__":
    app = FrameHistory(None)
    app.title('Initial')
    app.mainloop()