#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 16:01
# @Author  : zhangwen
# @File    : apt_test.py
# @Software: PyCharm

import warnings
import unittest
import paramunittest
from common.test_data_utils import TestDataUtils
from common.request_utils import RequestUtils

case_infos = TestDataUtils("Sheet1").def_testcase_data_list()

@paramunittest.parametrized(
    *case_infos
)

class ApiTest(paramunittest.ParametrizedTestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)

    def setParameters(self,case_id, case_info):
        """读取参数"""
        self.case_id = case_id
        self.case_info = case_info

    def test_api_common(self):
        """加载excel用例数据，执行用例，进行断言"""
        self._testMethodName = self.case_info[0].get("测试用例编号")
        self._testMethodDoc = self.case_info[0].get("测试用例名称")
        actual_result = RequestUtils().request_by_step(self.case_info)
        self.assertTrue(actual_result.get('check_result'))
if __name__ == "__main__":
    unittest.main()