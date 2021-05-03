from tkinter import *


class About(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("550x650+550+200")
        self.title("About us")
        self.resizable(False, False)

        self.top = Frame(self, height=550, widht=550, bg='purple')
        self.top.pack(fill=BOTH)

