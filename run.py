# -*- coding：utf-8 -*-
# @Time ：2022/1/3 10:08
# @Authon :hhj
# @Annotation:
# @File : run.py
import os
from datetime import datetime

import requests
from common.public.send_mail import SendMail

from common.public.do_excel import DoExcel
from common.public.do_config import DoConfig
from common.public.http_request import HttpRequest
from common.public import test_case
from BeautifulReport import BeautifulReport
from HwTestReport import HTMLTestReport
from common.public.project_path import *

import unittest

if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromModule(test_case))
    # with open('test_report.html', 'wb') as file:
    #     #runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title='测试报告', description='第一次测试报告', tester='hhj')
    #     runner = HTMLTestReport(stream=file, verbosity=2, title="单元测试报告", description="第一次报告", tester="hhj",
    #                             images=False)
    #     runner.run(suite)

    now = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    run = BeautifulReport(suite)
    path = test_report_path + '\测试报告' + str(now) + '.html'
    run.report(description='注册、登录、充值、加标、审核、投资模块', filename='\测试报告' + str(now),
               log_path=test_report_path)
    SendMail().send_mail(path)

# class run_case:
#     TOKEN = None
#     MEMBERID = None
#
#
#     def run_case(self, config_file_name, config_mode, excel_file_name, sheetname):
#         mode = DoConfig().read_config(config_file_name, 'MODE', config_mode)
#         print(mode)
#         test_data = DoExcel().read_excel(excel_file_name, sheetname, mode)
#
#         for itme in test_data:
#             if sheetname == 'recharge':
#                 itme['headers']['Authorization'] = getattr(run_case, 'TOKEN')
#                 if itme['data']['member_id'] == '登录获取':
#                     itme['data']['member_id'] = getattr(run_case, 'MEMBERID')
#             res = HttpRequest().http_request(itme['url'], itme['method'], itme['data'], itme['headers'])
#             if itme['case_id'] == 1 and itme['module'] == 'login' and res['code'] == 0:
#                 member_id = res['data']['id']
#                 token = res['data']['token_info']['token_type'] + ' ' + res['data']['token_info']['token']
#                 setattr(run_case, 'TOKEN', token)
#                 setattr(run_case, 'MEMBERID', member_id)
#
#             print(res)
#             print(itme['case_id'])
#             if res['code'] == itme['expected']['code'] and res['msg'] == itme['expected']['msg']:
#                 print(itme['case_id'])
#                 DoExcel().write_excel(excel_file_name, sheetname, itme['case_id'], str(res), 'pass')
#             else:
#                 DoExcel().write_excel(excel_file_name, sheetname, itme['case_id'], str(res), 'fail')
#
#
# if __name__ == '__main__':
#     run_case().run_case('common\\conf\\case.config', 'register_mode', 'test_data\\test_data.xlsx', 'register')
#     run_case().run_case('common\\conf\\case.config', 'login_mode', 'test_data\\test_data.xlsx', 'login')
#     run_case().run_case('common\\conf\\case.config', 'recharge_mode', 'test_data\\test_data.xlsx', 'recharge')

# 关于requests如何保持session会话：
# 1.创建一个session对象
# s = requests.session()
# 2.用创建的session对象发送各种请求：
# s.get(url, params=param)
# s.post(url, data=data)


# print(getattr(run_case, 'TOKEN'))
# mobile_phone = None
# mode = DoConfig().read_config('common\\conf\\case.config', 'MODE', 'mode')
# print(mode)
# test_data = DoExcel().read_excel('test_data\\test_data.xlsx', 'recharge', mode)
# for itme in test_data:
#     res = HttpRequest().http_request(itme['url'], itme['method'], itme['data'], itme['headers'])
#     # if itme['case_id'] == 2:
#     #     mobile_phone=itme['data']['mobile_phone']
#     #     print(mobile_phone)
#     print(res)
