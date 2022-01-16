# -*- coding：utf-8 -*-
# @Time ：2022/1/16 15:14
# @Authon :hhj
# @Annotation:
# @File : do_regx.py


import re

# s = 'www.baidu.com'
# res = re.match('(w)(ww)', s)  # 全匹配 头部匹配
# print(res.group())  # group()==group(0) 拿到匹配的全字符 分组 根据你的正则表达式里面的括号去分组

# s = '{"member_id": "${member_id}", "amount": 100}'
# res = re.findall('(me)(mber)', s)  # 列表 在字符串里面找匹配内容，存在列表里面
# #如果有分组，就是以元组的形式表现出来，列表嵌套元组
# print(res)
from common.public.get_data import GetData


class DoRegx:

    @staticmethod
    def do_regx(s):
        while re.search('\${(\w*)}', s):
            key = re.search('\${(\w*)}', s).group(0)
            value = re.search('\${(\w*)}', s).group(1)
            # print(key, value)
            if hasattr(GetData, value):
                s = s.replace(key, str(getattr(GetData, value)))
            else:
                break
            # print(key,value)
        return s


if __name__ == '__main__':
    s = '{"member_id": "${member_id}", "amount": "${amount}"}'
    res = DoRegx.do_regx(s)
    print(res)
