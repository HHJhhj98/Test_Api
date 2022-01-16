# -*- coding：utf-8 -*-
# @Time ：2022/1/3 22:46
# @Authon :hhj
# @Annotation:
# @File : test_case.py


import unittest

from common.public.do_excel import DoExcel
from common.public.get_data import GetData
from common.public.http_request import HttpRequest
from common.public.myddt import ddt, data
from common.public.read_data import ReadeData
from common.public.project_path import *
from common.public.my_log import MyLog
from common.public.do_mysql import DoMySql

my_logger = MyLog()

case_data = DoExcel().read_excel(test_data_path)


@ddt
class TestCase(unittest.TestCase):

    # def __init__(self, excel_file_name):
    #     super(TestCase, self).__init__('test_api')
    #     self.excel_file_name = excel_file_name

    def setUp(self):
        pass

    @data(*case_data)
    def test_api(self, case):
        if case['headers'].find('${token}') != -1:
            case['headers'] = case['headers'].replace('${token}', str(getattr(GetData, 'TOKEN')))
        if case['data'].find('${member_id}') != -1:
            case['data'] = case['data'].replace('${member_id}', str(getattr(GetData, 'MEMBERID')))
            case['data'] = eval(case['data'])
            if case['data']['member_id'] != ' ':
                case['data']['member_id'] = int(case['data']['member_id'])
        else:
            case['data'] = eval(case['data'])

        # if 'member_id' in case['data'].keys():
        #     if case['data']['member_id'] == '${loan_member_id}':
        #         case['data']['member_id'] = int(getattr(GetData, 'loan_member_id'))

        if 'loan_id' in case['data'].keys():
            if case['data']['loan_id'] == '${loan_id}':
                # case['data']['loan_id'] = getattr(GetData, 'LOANID')
                if getattr(GetData, 'LOANID') == None:
                    # case['data']['loan_id'] = getattr(GetData, 'LOANID')
                    query_sql = 'select max(l.id) from member as m,loan as l where m.id=l.member_id and m.mobile_phone={0}'.format(
                        getattr(GetData, 'loan_tel'))
                    loan_id = int(DoMySql().do_mysql(query_sql, 1)[0])
                    case['data']['loan_id'] = loan_id
                    setattr(GetData, 'LOANID', loan_id)
                else:
                    case['data']['loan_id'] = getattr(GetData, 'LOANID')

        print(case['data'])
        print(getattr(GetData, 'MEMBERID'))
        # res = HttpRequest().http_request(case['url'], case['method'], case['data'], eval(case['headers']))

        # print(case['check_sql_list'], type(case['check_sql_list']))

        if len(case['check_sql_list']):
            sql_res_list = []
            for i in range(len(case['check_sql_list'])):
                # print(case['check_sql_list'][i].format(case['data']['member_id']))
                # print(DoMySql().do_mysql(case['check_sql_list'][i].format(case['data']['member_id']), 1)[0])
                sql_res_list.append(
                    DoMySql().do_mysql(case['check_sql_list'][i].format(case['data']['member_id']), 1)[0])
            res = HttpRequest().http_request(case['url'], case['method'], case['data'], eval(case['headers']))
            sql_res_list.append(DoMySql().do_mysql(
                case['check_sql_list'][len(case['check_sql_list']) - 1].format(case['data']['member_id']), 1)[0])
            if abs(sql_res_list[len(sql_res_list) - 2] - sql_res_list[len(sql_res_list) - 1]) == case['data']['amount']:
                sql_res = 'pass'
            else:
                sql_res = 'fail'
            sql_res_list.append(sql_res)
            DoExcel().write_excel(filename=test_data_path, sheetname=case['module'], row=case['case_id'] + 1, col=11,
                                  result=str(sql_res_list))


        else:
            res = HttpRequest().http_request(case['url'], case['method'], case['data'], eval(case['headers']))
        # if case['module'] in getattr(GetData, 'check_list') and 'member_id' in case['data'].keys():
        #     if case['data']['member_id'] != '':
        #         # 请求之前查询余额
        #         query_sql = 'select leave_amount from member where id={}'.format(case['data']['member_id'])
        #         Before_Amount = DoMySql().do_mysql(query_sql, 1)[0]
        #         res = HttpRequest().http_request(case['url'], case['method'], case['data'], eval(case['headers']))
        #         After_Amount = DoMySql().do_mysql(query_sql, 1)[0]
        #         if res['code'] == 0:
        #             if abs(After_Amount - Before_Amount) == case['data']['amount']:
        #                 my_logger.info('{}模块，余额变动{}'.format(case['module'], case['data']['amount']))
        #             else:
        #                 my_logger.info('{}模块，余额变动{}'.format(case['module'], case['data']['amount']))
        #     else:
        #         res = HttpRequest().http_request(case['url'], case['method'], case['data'], eval(case['headers']))
        # else:
        #     res = HttpRequest().http_request(case['url'], case['method'], case['data'], eval(case['headers']))

        if case['case_id'] == 1 and case['module'] in ['recharge', 'loan_add', 'loan_audit', 'invest'] and res[
            'code'] == 0:
            member_id = res['data']['id']
            setattr(GetData, 'MEMBERID', member_id)
            token = res['data']['token_info']['token_type'] + ' ' + res['data']['token_info']['token']
            setattr(GetData, 'TOKEN', token)
        # elif case['case_id'] != 1 and case['module'] == 'loan_add' and res['code'] == 0:
        #     loan_id = res['data']['id']
        #     setattr(GetData, 'LOANID', loan_id)
        # elif case['case_id'] != 1 and case['module'] == 'loan_audit' and res['code'] == 0 and case['data'][
        #     'approved_or_not'] == 'true':
        #     loan_id = case['data']['loan_id']
        #     setattr(GetData, 'LOANID', loan_id)
        try:
            self.assertEqual(case['expected']['code'], res['code'])
            test_result = 'pass'
        except AssertionError as e:
            test_result = 'fail'
            my_logger.info("test_api_{0}'s error is {1},{2},{3}".format(case['title'], e, case['data'], res))
            # print("test_api_{0}'s error is {1}".format(case['data'], e))
            raise e
        finally:
            DoExcel().write_excel(filename=test_data_path, sheetname=case['module'], row=case['case_id'] + 1, col=9,
                                  result=str(res))
            DoExcel().write_excel(filename=test_data_path, sheetname=case['module'], row=case['case_id'] + 1, col=12,
                                  test_result=test_result)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
