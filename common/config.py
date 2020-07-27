#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/7/5 22:49
# @Author  : zhangwen
# @File    : config.py
# @Software: PyCharm
from common.setting_path import *
from common.config_utils import ConfigUtils

config_path = os.path.join( conf_path , 'config.ini' )

configUtils = ConfigUtils(config_path)
URL = configUtils.read_value( 'default','URL' )
CASE_DATA_PATH = configUtils.read_value( 'path','CASE_DATA_PATH' )
