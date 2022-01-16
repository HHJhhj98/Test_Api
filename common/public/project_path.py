# -*- coding：utf-8 -*-
# @Time ：2022/1/4 22:54
# @Authon :hhj
# @Annotation:
# @File : project_path.py

import os
from datetime import datetime

import common

'''专门来读取路径的值'''
project_path = os.path.split(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0])[0]

# cur_path = os.path.dirname(common.__file__)
#
# project_path = cur_path[:cur_path.find("Test_Api\\")+len("Test_Api\\")]

# 测试用例存放路径
test_data_path = os.path.join(project_path, 'test_data', 'test_data.xlsx')

# 配置文件存放路径
conf_path = os.path.join(project_path, 'common', 'conf', 'case.config')

# 测试报告存放路径
test_report_path = os.path.join(project_path, 'test_result', 'test_report')

now = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

# 日志存放路径
test_log_path = os.path.join(project_path, 'test_log', now + '_log.txt')

# print(cur_path)
print(project_path)
# print(cur_path.find("Test_Api\\"))

# print(test_path)
print(conf_path)
print(test_report_path)
