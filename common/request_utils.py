#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 19:31
# @Author  : zhangwen
# @File    : request_utils.py
# @Software: PyCharm
import requests
import ast
import re
from requests.exceptions import RequestException
from requests.exceptions import ProxyError
from requests.exceptions import ConnectionError
from common.localconfig_utils import local_config
from common.test_data_utils import TestDataUtils
import jsonpath
from common.check_data import CheckUtils
from common.test_data_utils import TestDataUtils
class RequestUtils:
    """主要负责接口请求处理"""
    def __init__(self):
        """初始化参数"""
        self.hosts = local_config.URL
        self.headers = {"ContentType": "application/json;charset=utf-8"}
        self.session = requests.session()
        self.temp_variables = {}

    def __get(self, get_infos):
        """处理get请求,get_info:请求数据 """
        try:
            url = self.hosts + get_infos['请求地址']


            response = self.session.get(url = url,
                                        params = ast.literal_eval(get_infos["请求参数(get)"])
                                        )

            response.encoding = response.apparent_encoding
            if get_infos["取值方式"] == "json取值":
                value = jsonpath.jsonpath( response.json(),get_infos["取值代码"] )[0]
                self.temp_variables[get_infos["传值变量"]] = value
            elif get_infos["取值方式"] == "正则取值":
                value = re.findall(get_infos["取值代码"], response.text)[0]
                self.temp_variables[get_infos["传值变量"]] = value
            result = CheckUtils(response).run_check(get_infos["期望结果类型"], get_infos["期望结果"])
        except ProxyError as e:
            result = {'code': 4, 'result': '[%s]请求：代理错误异常' % (get_infos["接口名称"])}
        except ConnectionError as e:
            result = {'code': 4, 'result': '[%s]请求：连接超时异常' % (get_infos["接口名称"])}
        except RequestException as e:
            result = {'code': 4, 'result': '[%s]请求：Request异常，原因：%s' % (get_infos["接口名称"], e.__str__())}
        except Exception as e:
            result = {'code':4,'result':'[%s]请求：系统异常，原因：%s'%(get_infos["接口名称"],e.__str__())}
        return result

    def __post(self, post_info):
        "处理post请求"
        try:
            url = self.hosts + post_info["请求地址"]
            response = self.session.post(url = url,
                                        headers = self.headers,
                                        params = ast.literal_eval(post_info["请求参数(get)"]),
                                         json = ast.literal_eval(post_info["提交数据（post）"])
            )
            if post_info["取值方式"] == "json取值":
                value = jsonpath.jsonpath( response.json(),post_info["取值代码"] )[0]
                self.temp_variables[ post_info["传值变量"] ] = value
            elif post_info["取值方式"] == "正则取值":
                value = re.findall(post_info["取值代码"],response.text)[0]
                self.temp_variables[post_info["传值变量"]] = value
            response.encoding = response.apparent_encoding
            result = CheckUtils(response).run_check(post_info["期望结果类型"], post_info["期望结果"])
        except ProxyError as e:
            result = {'code': 4, 'result': '[%s]请求：代理错误异常' % (post_info["接口名称"])}
        except ConnectionError as e:
            result = {'code': 4, 'result': '[%s]请求：连接超时异常' % (post_info["接口名称"])}
        except RequestException as e:
            result = {'code': 4, 'result': '[%s]请求：Request异常，原因：%s' % (post_info["接口名称"], e.__str__())}
        except Exception as e:
            result = {'code':4,'result':'[%s]请求：系统异常，原因：%s'%(post_info["接口名称"],e.__str__())}

        return result


    def request(self, step_info):
        """get post请求结合"""
        param_variable_list = re.findall('\\${\w+}', step_info["请求参数(get)"])
        if param_variable_list:
            for param_variable in param_variable_list:
                step_info["请求参数(get)"] = step_info["请求参数(get)"] \
                    .replace(param_variable, '"%s"' % self.temp_variables.get(param_variable[2:-1]))
        request_type = step_info["请求方式"]
        if request_type == "get":
            result = self.__get(step_info)
        elif request_type == "post":
            data_variable_list = re.findall('\\${\w+}', step_info["提交数据（post）"])
            if data_variable_list:
                for param_variable in data_variable_list:
                    step_info["提交数据（post）"] = step_info["提交数据（post）"] \
                        .replace(param_variable, '"%s"' % self.temp_variables.get(param_variable[2:-1]))
            result = self.__post(step_info)
        else:
            result = {'code':3, "result":"请求方式不支持"}
        return result

    def request_by_step(self, step_infos):
        self.temp_variables = {}
        #print(step_infos)
        for step_info in step_infos:
            temp_result = self.request(step_info)
            print(temp_result)
            if temp_result['code'] != 0:
                TestDataUtils("Sheet1").write_result_to_excel(step_infos['测试用例名称'],step_infos['测试用例编号'], '失败' )
                break
            else:
                TestDataUtils("Sheet1").write_result_to_excel(step_infos['测试用例名称'],step_infos['测试用例编号'])
            #print(temp_result['response_body'])
        return temp_result

if __name__ == "__main__":
   all_data = TestDataUtils("Sheet1").def_testcase_data_list()
   for case_info in all_data:
       RequestUtils().request_by_step(case_info.get("case_info"))



