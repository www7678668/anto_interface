#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/7/5 20:15
# @Author  : zhangwen
# @File    : setting_path.py
# @Software: PyCharm


"""配置所有文件的路径"""
import os


"""
获取当前文件路径  
os.path.abspath(__file__)--获取当前文件路径（包含文件）
os.path.dirname（path）--获取path的目录，去掉当前文件
"""
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#路径拼接，支持配置所有需要的路径
data_path = os.path.join(BASE_DIR, 'data')
conf_path = os.path.join(BASE_DIR, 'conf')
common_path = os.path.join(BASE_DIR, 'common')
testcase_path = os.path.join(BASE_DIR, "api_testcase")
test_report_path = os.path.join(BASE_DIR, "test_report")