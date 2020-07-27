#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 22:41
# @Author  : zhangwen
# @File    : xutils.py
# @Software: PyCharm

import os
import xlrd
from common.setting_path import *
from xlutils.copy  import copy

excel_path = os.path.join( data_path ,'test.xls' )
wb = xlrd.open_workbook( excel_path,formatting_info=True)  # 创建工作薄对象 xlrd模块2007 2003

# sheet = wb.sheet_by_name('Sheet1')
#
# print( sheet.cell_value(0,0) )

# new_workbook = copy(wb)  #
# sheet = new_workbook.get_sheet(wb.sheet_names().index('Sheet1'))
# sheet.write(2,4,'hsa')
# new_workbook.save(excel_path)


new_workbook = copy(wb)  #  new_workbook 已经变成可写的对象 xlwt 对象
sheet = new_workbook.get_sheet(wb.sheet_names().index('Sheet1'))
for i in range(1,6):
    sheet.write(i, 6, "奥术大师")
new_workbook.save(excel_path)
