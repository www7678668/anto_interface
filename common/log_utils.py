#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/7/6 22:05
# @Author  : zhangwen
# @File    : log_utils.py
# @Software: PyCharm

from common.setting_path import *
import time,os
import logging
from common.localconfig_utils import local_config
from common.setting_path import *
class LogUtils():
    def __init__(self):
        self.log_name = os.path.join( log_data_path ,'ApiTest_%s.log'%time.strftime('%Y_%m_%d') )
        self.logger = logging.getLogger("ApiTestLog")
        self.logger.setLevel( local_config.LOG_LEVEL )

        console_handler = logging.StreamHandler()  # 控制台输出
        file_handler = logging.FileHandler(self.log_name,'a',encoding='utf-8')  # 文件输出
        formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        self.logger.addHandler( console_handler )
        self.logger.addHandler( file_handler )

        console_handler.close()  # 防止打印日志重复
        file_handler.close()     # 防止打印日志重复

    def get_logger(self):
        return self.logger

logger = LogUtils().get_logger()   # 防止打印日志重复

if __name__ == '__main__':
    logger.info('hello55666')
