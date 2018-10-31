# -*- coding: utf-8 -*-
import configparser


def getPropertyVal(section, key):
    config = configparser.ConfigParser()
    config.read('dev/config.ini')
    return config.get(section, key)