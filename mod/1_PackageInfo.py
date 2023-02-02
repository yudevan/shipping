from tkinter import *
from lib.module import *


class PackageInfo(FixedHModule, FieldManager, object):
    modconf = ModConfig()
    modconf.Label = "Package Information"
    modconf.field_prefix = ""
    modconf.fields = {
        "length": {
            "type": modconf.FieldType.INT,
            "label": "Length [cm]",
        },
        "width": {
            "type": modconf.FieldType.INT,
            "label": "Width [cm]",
        },
        "height": {
            "type": modconf.FieldType.INT,
            "label": "Height [cm]",
        },
        "weight": {
            "type": modconf.FieldType.FLOAT,
            "label": "Weight [pound]",
        },
        "dimension": {
            "type": modconf.FieldType.LINE,
            "label": "Dimension",
        },
    }

    def __init__(self, master=None, *args, **kwargs):
        super(PackageInfo, self).__init__(master, *args, **kwargs)
        FieldManager.__init__(self, self, self.modconf.fields)
        self.fields_value['dimension'].set("0x0x0")
        self.fields_value['length'].trace(
            "w",
            lambda name, index, mode: self.updateDimension(name, index, mode),
        )
        self.fields_value['width'].trace(
            "w",
            lambda name, index, mode: self.updateDimension(name, index, mode),
        )
        self.fields_value['height'].trace(
            "w",
            lambda name, index, mode: self.updateDimension(name, index, mode),
        )

    def updateDimension(self, name, index, mode):
        self.fields_value["dimension"].set("{}x{}x{}".format(
            self.fields_value['length'].get(),
            self.fields_value['width'].get(),
            self.fields_value['height'].get()))
