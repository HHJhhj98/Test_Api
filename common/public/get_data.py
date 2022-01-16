# -*- coding：utf-8 -*-
# @Time ：2022/1/5 21:30
# @Authon :hhj
# @Annotation:
# @File : get_data.py

# -*- coding：utf-8 -*-
# @Time ：2022/1/3 22:48
# @Authon :hhj
# @Annotation:
# @File : get_attr.py

from common.public import project_path
import pandas as pd
from common.public.do_config import DoConfig


class GetData:
    TOKEN = None
    MEMBERID = None
    EXCELFILENAMA = None
    df = pd.DataFrame(pd.read_excel(project_path.test_data_path, sheet_name='init'))
    NoRegTel = df.loc[:]['测试数据'][0]
    normal_tel = df.loc[:]['测试数据'][1]
    admin_tel = df.loc[:]['测试数据'][2]
    loan_tel = df.loc[:]['测试数据'][3]
    loan_member_id = df.loc[:]['测试数据'][4]
    loan_member_id = df.loc[:]['测试数据'][4]
    LOANID = None
    check_list = eval(DoConfig().read_config(project_path.conf_path, 'CHECKLEAVEAMOUNT', 'check_list'))
    amount = 100

# print(str(getattr(GetData, 'ADMIN_TEL')), type(getattr(GetData, 'ADMIN_TEL')))
