#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 15:25
# @Author  : zhangwen
# @File    : paramuunittest_demo.py
# @Software: PyCharm

import paramunittest
import unittest
from common.test_data_utils import TestDataUtils

all_data_excel = TestDataUtils("Sheet1").def_testcase_data_list()
# @paramunittest.parametrized(
#     (8,5),
#     (10,20)
# )
@paramunittest.parametrized(
    *all_data_excel
)

class UTestDemo(paramunittest.ParametrizedTestCase):
    def setParameters(self, case_id, case_info):
        self.case_id = case_id
        self.case_info = case_info

    def test_number(self):
        print("case_id = %s, case_info = %s"%(self.case_id, self.case_info))
        self.assertGreater(self.numa, self.numb)


if __name__ == "__main__":
    unittest.main()

