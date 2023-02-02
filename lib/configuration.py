import os
import sys
import logging
import shelve
import json


class Config(object):
    AppName = "Shipping"
    AppTitle = "Shipping Label Creator"
    __instance = None

    @staticmethod
    def getConfig():
        return Config.__instance if Config.__instance else Config()

    def __init__(self):
        super(Config, self).__init__()
        self.postdata = {}
        self.fields_label = {}
        self.fields_value = {}
        self.form_fields = {}
        with open(os.path.join(sys.path[0], "data/address.json")) as f:
            self.data = json.load(f)

        self.logger = logging.getLogger(self.AppName)
        logging.basicConfig(
            filename=os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                  '{}.log'.format(self.AppName)),
            format=
            '%(asctime)s  %(name)s  %(levelname)s %(filename)s: %(message)s',
            level=logging.DEBUG)
        self.consoleHandler = logging.StreamHandler()
        self.consoleHandler.setLevel(logging.INFO)
        formatter = logging.Formatter(
            '%(asctime)s  %(name)s  %(levelname)s: %(message)s')
        self.consoleHandler.setFormatter(formatter)
        self.logger.addHandler(self.consoleHandler)
        Config.__instance = self