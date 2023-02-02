from lib.application import Application
from lib.module import *

from mod import *

if __name__ == "__main__":
    app = Application()
    modules = [mod(app.vpanel) for mod in VModule.__subclasses__()]
    bottom_modules = [bmod(app.bottomframe) for bmod in FixedHModule.__subclasses__()]
    for mod in modules:
        app.vpanel.add(mod, stretch="always")

    for i, bmod in enumerate(bottom_modules):
        bmod.grid(row=0, column=i, sticky=NSEW)

    app.mainloop()
