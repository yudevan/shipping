import os
import sys
import json
from tkinter import *
from tkinter import ttk
from .configuration import Config
import requests


class FieldManager(object):

    def __init__(self, master=None, fields={}):
        super(FieldManager, self).__init__()
        self.master = master
        self.fields = fields
        self.config = Config.getConfig()
        self.fields_label = self.config.fields_label
        self.fields_value = self.config.fields_value
        self.form_fields = self.config.form_fields
        self.trace_event = "wua"
        row = 2
        for i, fld in enumerate(self.fields):
            # ttk.Combobox(ship_from_frame, values=options)
            tmp_field = "{}{}".format(self.master.modconf.field_prefix, fld)
            if self.fields[fld]["type"] == self.master.modconf.FieldType.LINE:
                self.fields_value[tmp_field] = StringVar(name=tmp_field)
                self.fields_value[tmp_field].trace(
                    self.trace_event,
                    lambda name, index, mode, widget=self.fields_value[
                        tmp_field]: self.variableChange(widget),
                )
                self.fields_label[tmp_field] = Label(
                    self.master, text=self.fields[fld]["label"])
                self.form_fields[tmp_field] = Entry(
                    self.master, textvariable=self.fields_value[tmp_field])
            elif self.fields[fld][
                    "type"] == self.master.modconf.FieldType.TEXT:
                self.fields_value[tmp_field] = StringVar(name=tmp_field)
                self.fields_value[tmp_field].trace(
                    self.trace_event,
                    lambda name, index, mode, widget=self.fields_value[
                        tmp_field]: self.variableChange(widget),
                )
                self.fields_label[tmp_field] = Label(
                    self.master, text=self.fields[fld]["label"])
                self.form_fields[tmp_field] = Text(self.master, height=4)
            elif self.fields[fld][
                    "type"] == self.master.modconf.FieldType.OPTIONS:
                self.fields_value[tmp_field] = StringVar(name=tmp_field)

                self.fields_label[tmp_field] = Label(
                    self.master, text=self.fields[fld]["label"])
                self.form_fields[tmp_field] = ttk.Combobox(
                    self.master,
                    textvariable=self.fields_value[tmp_field],
                    state="readonly")  # values=

                if fld == "saved_address":
                    options = [opt for opt in self.config.data[fld].keys()]
                    self.form_fields[tmp_field].configure(values=options,
                                                          state="readonly")
                    self.form_fields[tmp_field].current(0)
                    self.fields_value[tmp_field].trace(
                        self.trace_event,
                        lambda name, index, mode, widget=self.form_fields[
                            tmp_field], wval=self.fields_value[tmp_field]: self
                        .saved_address_callback(widget, wval),
                    )

                elif fld == "shipper":
                    options = [opt for opt in self.config.data[fld].keys()]
                    self.form_fields[tmp_field].configure(values=options,
                                                          state="readonly")
                    self.form_fields[tmp_field].current(0)
                    self.fields_value[tmp_field].trace(
                        self.trace_event,
                        lambda name, index, mode, widget=self.form_fields[
                            tmp_field], wval=self.fields_value[tmp_field]: self
                        .shipper_callback(widget, wval),
                    )
                    self.form_fields[tmp_field].bind('<<ComboboxSelected>>',
                                                     None)

            elif self.fields[fld][
                    "type"] == self.master.modconf.FieldType.BOOL:
                self.fields_value[tmp_field] = BooleanVar(name=tmp_field)
                self.fields_value[tmp_field].trace(
                    self.trace_event,
                    lambda name, index, mode, widget=self.fields_value[
                        tmp_field]: self.variableChange(widget),
                )
                self.fields_label[tmp_field] = Label(
                    self.master, text=self.fields[fld]["label"])
                self.form_fields[tmp_field] = Checkbutton(
                    self.master,
                    text=self.fields[fld]["label"],
                    variable=self.fields_value[tmp_field],
                    onvalue=1,
                    offvalue=0,
                )
            elif self.fields[fld]["type"] == self.master.modconf.FieldType.INT:
                self.fields_value[tmp_field] = IntVar(name=tmp_field)
                self.fields_value[tmp_field].trace(
                    self.trace_event,
                    lambda name, index, mode, widget=self.fields_value[
                        tmp_field]: self.variableChange(widget),
                )
                self.fields_label[tmp_field] = Label(
                    self.master, text=self.fields[fld]["label"])
                self.form_fields[tmp_field] = Spinbox(
                    self.master,
                    from_=0,
                    to=1000,
                    textvariable=self.fields_value[tmp_field],
                    text=self.fields_value[tmp_field])
            elif self.fields[fld][
                    "type"] == self.master.modconf.FieldType.FLOAT:
                self.fields_value[tmp_field] = DoubleVar(name=tmp_field)
                self.fields_value[tmp_field].trace(
                    self.trace_event,
                    lambda name, index, mode, widget=self.fields_value[
                        tmp_field]: self.variableChange(widget),
                )
                self.fields_label[tmp_field] = Label(
                    self.master, text=self.fields[fld]["label"])
                self.form_fields[tmp_field] = Spinbox(
                    self.master,
                    from_=0.0,
                    to=1000.0,
                    textvariable=self.fields_value[tmp_field],
                    text=self.fields_value[tmp_field],
                )
            else:
                self.fields_value[tmp_field] = StringVar(name=tmp_field)
                self.fields_value[tmp_field].trace(
                    self.trace_event,
                    lambda name, index, mode, widget=self.fields_value[
                        tmp_field]: self.variableChange(widget),
                )
                self.fields_label[tmp_field] = Label(
                    self.master, text=self.fields[fld]["label"])
                self.form_fields[tmp_field] = Entry(
                    self.master, textvariable=self.fields_value[tmp_field])

            self.fields_label[tmp_field].grid(row=row,
                                              column=0,
                                              columnspan=4,
                                              sticky=W)
            if self.fields[fld]["type"] == self.master.modconf.FieldType.BOOL:

                self.form_fields[tmp_field].grid(row=row + 1,
                                                 column=0,
                                                 columnspan=4,
                                                 sticky=W)
            else:
                self.form_fields[tmp_field].grid(row=row + 1,
                                                 column=0,
                                                 columnspan=4,
                                                 sticky=EW)
            row += 2

    def getValues(self):
        pass

    def variableChange(self, widget):
        pass

    def saved_address_callback(self, widget, wval):
        index = widget.current()
        print("============\nWidget:", widget.get(), index, wval.get())

        for k, v in self.config.data["saved_address"][wval.get()].items():
            tmp_field = "{}{}".format(self.master.modconf.field_prefix, k)
            print(k, v, tmp_field)
            self.fields_value[tmp_field].set(v)

    def service_value_callback(self, widget, wval):
        index = widget.current()
        print("============\nServiceValue:", widget.get(), index, wval.get())

        for k, v in self.config.data["shipper"][
                self.fields_value["shipper"].get()].items():
            for i, j in v.items():

                tmp_field = "{}{}".format(self.master.modconf.field_prefix, i)
                if hasattr(self.fields_value, tmp_field):
                    self.fields_value[tmp_field].set(j)

    def shipper_callback(self, widget, wval):
        index = widget.current()
        print("============\nShipper:", widget.get(), index, wval.get())
        svcoptions = []
        accoptions = []
        # Read dictionary belong to the current wval
        for k, v in self.config.data["shipper"][wval.get()].items():
            svcoptions.append(k)
        # set the Service based on selected Provider
        self.form_fields["shipping_service"].configure(values=svcoptions,
                                                       state="readonly")
        self.form_fields["shipping_service"].current(0)

        self.fields_value["shipping_service"].trace(
            self.trace_event,
            lambda name, index, mode, widget=self.
            form_fields["shipping_service"], wval=self.fields_value[
                "shipping_service"]: self.service_value_callback(widget, wval),
        )

        for x, y in self.config.data["shipping_account"][wval.get()].items():
            print(x, y)
            accoptions.append(x)
        # set the Service based on selected Provider
        self.form_fields["shipping_account"].configure(values=accoptions,
                                                       state="readonly")
        self.form_fields["shipping_account"].current(0)
        self.fields_value["shipping_account"].trace(
            self.trace_event,
            lambda name, index, mode, widget=self.form_fields[
                "shipping_account"], wval=self.fields_value[
                    "shipping_account"]: self.account_callback(widget, wval),
        )

    def account_callback(self, widget, wval):
        index = widget.current()
        print("============\nAccount:", widget.get(), index, wval.get())

    def postRequest(self):
        data = {}
        for k, v in self.fields_value.items():
            data[k] = v.get()
        #requests.post("https://hooks.zapier.com/hooks/catch/12773137/b77kqrm/",json=data)


class ModConfig(object):
    Name = "default"
    Label = "default"
    Checkable = False
    HeaderBG = "lightgreen"
    HeaderRelief = RAISED
    HeaderFont = ("Arial", 18, "bold")

    class FieldType:
        LINE, TEXT, INT, FLOAT, BOOL, OPTIONS = range(0, 6)

    field_prefix = "ship_from_"
    fields = {
        "saved_address": {
            "type": FieldType.OPTIONS,
            "label": "Saved Address",
        },
        "name": {
            "type": FieldType.LINE,
            "label": "Name",
        },
        "address": {
            "type": FieldType.LINE,
            "label": "Address",
        },
        "city": {
            "type": FieldType.LINE,
            "label": "City",
        },
        "state": {
            "type": FieldType.OPTIONS,
            "label": "State",
        },
        "zip": {
            "type": FieldType.LINE,
            "label": "Zip Code",
        },
        "phone": {
            "type": FieldType.LINE,
            "label": "Phone",
        },
        "email": {
            "type": FieldType.LINE,
            "label": "Email",
        },
    }


class VModule(LabelFrame):
    modconf = ModConfig()

    def __init__(self, master=None, *args, **kwargs):
        LabelFrame.__init__(self, master, *args, **kwargs)

        self.configure(text=self.modconf.Label, height=300, padx=0, pady=0)
        self.rowconfigure(20, weight=1)
        self.columnconfigure(2, weight=1)

        if self.modconf.Checkable:
            self.modCheck = Checkbutton(self,
                                        text=self.modconf.Label,
                                        padx=0,
                                        pady=0)
            self.configure(labelwidget=self.modCheck)

        self.label = Label(
            self,
            text=self.modconf.Label,
            background=self.modconf.HeaderBG,
            font=self.modconf.HeaderFont,
            relief=self.modconf.HeaderRelief,
        )
        self.label.grid(row=0, column=0, columnspan=3, sticky=NSEW)

        self.row = 1
        self.col = 0


class FixedHModule(LabelFrame):
    modconf = ModConfig()

    def __init__(self, master=None, *args, **kwargs):
        LabelFrame.__init__(self, master, *args, **kwargs)

        self.rowconfigure(20, weight=1)
        self.columnconfigure(4, weight=1)
        self.configure(text=self.modconf.Label)
        self.configure(height=400)

        if self.modconf.Checkable:
            self.modCheck = Checkbutton(self, text=self.modconf.Label, padx=5)
            self.configure(labelwidget=self.modCheck)

        self.label = Label(
            self,
            text=self.modconf.Label,
            background=self.modconf.HeaderBG,
            font=self.modconf.HeaderFont,
            relief=self.modconf.HeaderRelief,
        )
        self.label.grid(row=0, column=0, columnspan=3, sticky=NSEW)

        self.row = 1
        self.col = 0
