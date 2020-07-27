#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/7/6 22:16
# @Author  : zhangwen
# @File    : login_requests.py
# @Software: PyCharm

import requests
import requests
import re

hosts = 'http://47.107.178.45'
session = requests.session()  #创建session对象
session_ = requests.session()
get_registet_params = {
    "m": "u",
    "c": "register"
}
register_page = session.get( url = hosts+"/phpwind/index.php",
                     params = get_registet_params )
body01 = register_page.content.decode('utf-8')
token_id = re.findall( 'name="csrf_token" value="(.+?)"/>',body01)[0]

print(token_id)

get_registet_submit_params = {
    "m": "u",
    "c": "register",
    "a": "dorun"

}
post_registet_data={
    "username":"wwwww123457",
    "password":"zxw605686114",
    "repassword":"zxw605686114",
    "email":"60555574@qq.com",
    "csrf_token":token_id
}
register_submit =session.post(url = hosts + "/phpwind/index.php",
                    params = get_registet_submit_params,
                    data= post_registet_data,
                    )
#
print( register_submit.content.decode('utf-8') )
