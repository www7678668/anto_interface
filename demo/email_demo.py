#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 16:30
# @Author  : zhangwen
# @File    : email_demo.py
# @Software: PyCharm

import smtplib
from email.mime.text import MIMEText

# body_str = '''
# <h3 align="center">自动化测试报告</h3>
# <table border="2" align="center" width="50%",height="400">
# <tr><td></td><td></td><td></td><td></td></tr>
# <tr><td></td><td></td><td></td><td></td></tr>
# <tr><td></td><td></td><td></td><td></td></tr>
# <tr><td></td><td></td><td></td><td></td></tr>
# </table>
# '''
#
# msg = MIMEText(body_str, "html", "utf-8")
# msg["from"] = "605686114@qq.com"
# msg["to"] = "605686114@qq.com"
# msg["Cc"] = "605686114@qq.com"
# msg["subject"] = "自动化接口学习"
#
# smtp = smtplib.SMTP()
# smtp.connect("smtp.qq.com")
# smtp.login(user="605686114@qq.com", password="ccuyhrofhjwabfbh")
# smtp.sendmail( "605686114@qq.com",["605686114@qq.com"],msg.as_string() )



