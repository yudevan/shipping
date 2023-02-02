from tkinter import *
from lib.module import *


class Creation(FixedHModule, FieldManager, object):
    modconf = ModConfig()
    modconf.Label = "Label Creation"
    modconf.field_prefix = ""
    modconf.fields = {
        "print_label": {
            "type": modconf.FieldType.BOOL,
            "label": "Print Label",
        },
        "fetch_label_url": {
            "type": modconf.FieldType.BOOL,
            "label": "Fetch Label URL",
        },
    }

    def __init__(self, master=None, *args, **kwargs):
        super(Creation, self).__init__(master, *args, **kwargs)
        FieldManager.__init__(self, self, self.modconf.fields)
        self.create_button = Button(self,
                                    text="Create Label(s)",
                                    font=("Arial", 14, "bold"),
                                    command=lambda: self.postRequest())

        self.create_button.grid(row=10, column=1, padx=5, pady=5)
