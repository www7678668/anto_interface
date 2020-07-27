#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 13:16
# @Author  : zhangwen
# @File    : importdata_demo.py
# @Software: PyCharm

from common.test_data_utils import TestDataUtils

all_data = TestDataUtils("Sheet1").def_testcase_data_list()
for excel_data in all_data:
    print(excel_data.get("case_info"))