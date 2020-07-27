#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 16:25
# @Author  : zhangwen
# @File    : runn_case.py
# @Software: PyCharm

import os
import unittest
from common.localconfig_utils import local_config
from common import HTMLTestReportCN
from common.email_Utils import EmailUtils
from common.setting_path import *

class RunCase:
    def __init__(self):
        self.test_case_path = testcase_path
        self.test_report_path = test_report_path
        self.title = 'P1P2接口自动化测试报告'
        self.description = '自动化接口测试框架学习用'
        self.tester = '测试开发组全体成员'

    def load_test_suite(self):
        discover = unittest.defaultTestLoader.discover(start_dir=self.test_case_path,
                                                       pattern='apt_test.py',
                                                       top_level_dir=self.test_case_path)
        all_suite = unittest.TestSuite()
        all_suite.addTest( discover )
        return all_suite

    def run_case(self):
        """执行用例"""
        report_dir = HTMLTestReportCN.ReportDirectory(self.test_report_path)
        report_dir.create_dir(self.title)
        report_file_path = HTMLTestReportCN.GlobalMsg.get_value("report_path")
        fp = open(report_file_path, 'wb')
        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                                 title=self.title,
                                                 description=self.description,
                                                 tester=self.tester)
        runner.run(self.load_test_suite())
        fp.close()
        return report_file_path

if __name__ == "__main__":
    report_path = RunCase().run_case()
    EmailUtils(open(report_path, 'rb').read(), report_path).send_mail()