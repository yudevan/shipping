from tkinter import *
from lib.module import *


class ReturnAddress(VModule, FieldManager, object):
    modconf = ModConfig()
    modconf.Checkable = True
    modconf.Label = "Shipping Return Address"
    modconf.field_prefix = 'return_'

    def __init__(self, master=None, *args, **kwargs):
        super(ReturnAddress, self).__init__(master, *args, **kwargs)
        FieldManager.__init__(self, self, self.modconf.fields)
