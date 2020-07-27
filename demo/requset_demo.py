#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 20:23
# @Author  : zhangwen
# @File    : requset_demo.py
# @Software: PyCharm

import requests
host = "https://api.weixin.qq.com/cgi-bin/token"
get_params ={
    "grant_type":"client_credential",
    "appid":"wx4ee1b29645113dcd",
    "secret":"7644ab6fb399d7fa70dc38191c205ec4"
}

response = requests.get(url = host,
                        params = get_params

)
print(response.content.decode("utf-8"))