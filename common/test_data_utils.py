#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/7/5 21:36
# @Author  : zhangwen
# @File    : test_data_utils.py
# @Software: PyCharm

import os
from common.setting_path import *
from common.excel_utils import readExcelXlrd
from common.sql_utlis import SqlUtils
excel_path = os.path.join(data_path,'test_case.xls')
excelUtils = readExcelXlrd(excel_path,'Sheet1')
class TestDataUtils:
    """把获取的excel数据转化为我们需要的数据格式"""

    def __init__(self, sheet_name,test_data_path = excel_path):
        """初始化文件路径，需要处理的数据"""
        self.test_data_path = test_data_path
        self.sheet_name = sheet_name
        self.test_data_sheet = readExcelXlrd(self.test_data_path, self.sheet_name)
        self.test_data = self.test_data_sheet.get_sheet_by_dict() # excel 数据源
        self.test_data_by_mysql = SqlUtils().get_mysql_test_case_info()  #mysql数据源

    def __get_testcase_data_dict(self):
        """返回一个包含excel该sheet页的所有数据，以字典的形式"""
        testcase_dict = {}
        for row_data in self.test_data:
            if row_data["用例执行"] == '是':
                testcase_dict.setdefault( row_data['测试用例编号'],[] ).append( row_data )
        return testcase_dict

    def def_testcase_data_list(self):
        """把获取的数据进行重新构造，构造成[{},{}]方便后续使用"""
        testcase_list = []
        for k, v in self.__get_testcase_data_dict().items():
            one_case_dict = {}
            one_case_dict["case_id"] = k
            one_case_dict["case_info"] = v
            testcase_list.append(one_case_dict)
        return testcase_list



    def __get_testcase_data_dict_by_mysql(self):
        """mysql数据转换为字典"""
        testcase_dict = {}
        for row_data in self.test_data_by_mysql:
            testcase_dict.setdefault( row_data['测试用例编号'],[] ).append( row_data )
        return testcase_dict

    def def_testcase_data_list_by_mysql(self):
        """读取mydql的所有数据"""
        testcase_list = []
        for k,v in self.__get_testcase_data_dict_by_mysql().items():
            one_case_dict = {}
            one_case_dict["case_id"] = k
            one_case_dict["case_info"] = v
            testcase_list.append( one_case_dict )
        return tuple(testcase_list)

    def get_row_num(self,case_id,case_step_name):
        for j in range(len(self.test_data)):
            if self.test_data[j]['测试用例编号'] == case_id and self.test_data[j]['测试用例步骤'] == case_step_name:
                break
        return j+1

    def get_result_id(self):
        for col_id in range(len(self.test_data_sheet.sheet.row(0))):
            if self.test_data_sheet.sheet.row(0)[col_id].value == '测试结果':
                break
        return col_id


    def write_result_to_excel(self, case_id, case_name, content="通过"):
        """把测试结果写入excel中"""
        row_id = self.get_row_num(case_id, case_name)
        self.test_data_sheet.update_excel_data(row_id, 14, content)


    def clear_result_from_excel(self):
      """清除测试结果"""
      row_count = self.test_data_sheet.get_row_count()
      col_id = self.get_result_id
      self.test_data_sheet.clear_excel_cloumn(1,row_count,col_id)

if __name__ == "__main__":
    testdataUtils = TestDataUtils("Sheet1")
    # for i in testdataUtils.def_testcase_data_list():
    #     print(i)

    row = testdataUtils.def_testcase_data_list_by_mysql()
    print(row)
