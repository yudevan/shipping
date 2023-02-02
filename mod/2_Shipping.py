from tkinter import *
from lib.module import *


class Shipping(FixedHModule, FieldManager, object):
    modconf = ModConfig()
    modconf.Label = "Shipping Authorization"
    modconf.field_prefix = ""
    modconf.fields = {
        "shipper": {
            "type": modconf.FieldType.OPTIONS,
            "label": "Shipper",
        },
        "shipping_service": {
            "type": modconf.FieldType.OPTIONS,
            "label": "Service",
        },
        "shipping_account": {
            "type": modconf.FieldType.OPTIONS,
            "label": "Account",
        },
        "adult_signature_required": {
            "type": modconf.FieldType.BOOL,
            "label": "Signature Required",
        },
        "num_labels": {
            "type": modconf.FieldType.INT,
            "label": "Number Of identical Label",
        },
    }

    def __init__(self, master=None, *args, **kwargs):
        super(Shipping, self).__init__(master, *args, **kwargs)
        FieldManager.__init__(self, self, self.modconf.fields)
