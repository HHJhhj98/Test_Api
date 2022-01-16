# -*- coding：utf-8 -*-
# @Time ：2022/1/9 21:20
# @Authon :hhj
# @Annotation:
# @File : do_mysql.py

# 关键字参数

import mysql.connector
from common.public.do_config import DoConfig
from common.public.project_path import *
from common.public.my_log import MyLog

my_logger = MyLog()
class DoMySql:

    def do_mysql(self, query_sql, state='all'):
        db_config = eval(DoConfig().read_config(conf_path, 'DB', 'db_config'))

        # 创建一个数据库连接
        cnn = mysql.connector.connect(**db_config)

        # 新建一个游标cursor
        cursor = cnn.cursor()

        # # 写sql语句
        # query_sql = 'select max(mobile_phone) from member where mobile_phone like "138%"'

        # 执行语句
        cursor.execute(query_sql)

        # 获取结果
        if state == 1:
            res = cursor.fetchone()  # 针对一行数据，返回值为元组 (3, '小柠檬3', '25D55AD283AA400AF464C76D713C07AD', '15889218362', 1, Decimal('240.00'), datetime.datetime(2021, 12, 24, 20, 1, 4))
        else:
            res = cursor.fetchall()  # 针对多行数据，返回值为列表嵌套元组
        # print(res)
        # print(int(res[0]) + 1)

        # 关闭游标
        cursor.close()

        # 关闭连接
        cnn.close()
        my_logger.info('执行sql：'+query_sql+'的返回结果为'+str(res))
        return res


if __name__ == '__main__':
    from common.public.get_data import GetData
    query_sql = 'select max(id) from loan where member_id={0}'.format(getattr(GetData,'loan_member_id'))
    res = DoMySql().do_mysql(query_sql, 1)
    print(res)
    print(res[0],type(res[0]))
