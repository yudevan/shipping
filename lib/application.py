from tkinter import *
from .uicomponents import *
from .configuration import Config
from .module import FieldManager


class FormManager(object):
    def __init__(self):
        self.moduleManager = [child() for child in FieldManager.__subclasses__()]

        for cld in self.moduleManager:
            for key, value in cld.fields_value.items():
                print(key, value.get())


class Application(Tk):
    def __init__(
        self, screenName=None, baseName=None, className="Tk", useTk=1, sync=0, use=None
    ):
        Tk.__init__(self, screenName, baseName, className, useTk, sync, use)
        self.conf = Config.getConfig()
        self.title(self.conf.AppTitle)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(3, weight=1)
        self.width = 640
        self.height = 500
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - self.width) / 2
        y = (sh - self.height) / 2
        self.geometry("%dx%d+%d+%d" % (self.width, self.height, x, y))
        # self.resizable(width=False, height=False)

        self.menu = Menu(self, relief="groove")
        self.locationmenu = Menu(self.menu)
        self.config(menu=self.menu)
        self.topvscroll = Scrollbar(self, orient=VERTICAL)
        self.topvscroll.grid(row=0, column=1, rowspan=2, sticky=NS)
        self.mainframe = Canvas(self, yscrollcommand=self.topvscroll.set)
        self.mainframe.rowconfigure(4, weight=1)
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.grid(row=0, column=0, sticky=NSEW)
        self.topvscroll.config(command=self.mainframe.yview)

        self.statusbar = StatusBar(self, relief="sunken")
        self.statusbar.grid(row=2, column=0, sticky=EW)

        topmenu = ["File", "View", "Help"]

        for m in topmenu:
            self.menu.add_command(label=m, font="Arial 11")
        self.topframe = MainFrame(self.mainframe)
        self.topframe.rowconfigure(4, weight=1)
        self.topframe.columnconfigure(0, weight=1)
        self.bottomframe = MainFrame(self.mainframe)
        self.bottomframe.rowconfigure(4, weight=1)
        self.bottomframe.columnconfigure(4, weight=1)
        self.vpanel = PanedWindow(
            self.topframe,
            orient=HORIZONTAL,
            borderwidth=5,
        )
        self.vpanel.grid(row=0, column=0, sticky=NSEW)

        self.topframe.grid(row=0, column=0, sticky=NSEW)
        self.bottomframe.grid(row=1, column=0, sticky=NSEW)

        modman = FormManager()
