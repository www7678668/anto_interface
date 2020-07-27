#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 0:08
# @Author  : zhangwen
# @File    : re_demo.py
# @Software: PyCharm

import re
pattern = re.compile(r'\d+')
print(pattern.split( 'newdream55nssewdsds66newd5555ream '))
print(re.split('\d+', 'newdream55nssewdsds66newd5555ream '))


