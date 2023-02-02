from tkinter import *
from lib.module import *


class FromAddress(VModule, FieldManager, object):
    modconf = ModConfig()
    modconf.Label = "Shipping From Address"
    modconf.field_prefix = 'ship_from_'

    def __init__(self, master=None, *args, **kwargs):
        super(FromAddress, self).__init__(master, *args, **kwargs)
        FieldManager.__init__(self, self, self.modconf.fields)
