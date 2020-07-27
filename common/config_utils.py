#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/7/5 22:24
# @Author  : zhangwen
# @File    : config_utils.py
# @Software: PyCharm

import configparser


class ConfigUtils():
    def __init__(self, config_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(config_path,encoding="utf-8")

    def read_value(self, section, key):
        value = self.cfg.get(section, key)
        return value
