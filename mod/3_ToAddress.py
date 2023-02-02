from tkinter import *
from lib.module import *


class ToAddress(VModule, FieldManager, object):
    modconf = ModConfig()
    modconf.Label = "Shipping To Address"
    modconf.field_prefix = 'ship_to_'

    def __init__(self, master=None, *args, **kwargs):
        super(ToAddress, self).__init__(master, *args, **kwargs)
        FieldManager.__init__(self, self, self.modconf.fields)
