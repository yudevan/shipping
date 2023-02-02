from tkinter import *


class VerticalFrame(PanedWindow):

    def __init__(self, master, **kw):
        PanedWindow.__init__(self, orient=VERTICAL)


class StatusBar(Frame):

    def __init__(self, master=None, **kw):
        Frame.__init__(self, master, **kw)


class MainFrame(Frame):

    def __init__(self, master=None, **kw):
        Frame.__init__(self, master, **kw)