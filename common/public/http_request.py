# -*- coding：utf-8 -*-
# @Time ：2022/1/3 10:09
# @Authon :hhj
# @Annotation:requests get、post请求封装
# @File : http_request.py


import requests
from common.public.my_log import MyLog

my_logger = MyLog()


class HttpRequest:
    def http_request(self, url, method, data=None, headers=None):
        '''
            url:请求地址 http：xxx：port
            data：传递参数，非必填，字典的格式传递参数
            headers：非必填
            method:请求方式：get、post
            :return: 响应的json结果
        '''
        try:
            if method.lower() == 'get':
                res = requests.get(url=url, data=data, headers=headers)
            elif method.lower() == 'post':
                res = requests.post(url=url, json=data, headers=headers)
            elif method.lower() == 'patch':
                res = requests.request(method=method.lower(), url=url, json=data, headers=headers)
            else:
                res = None
                my_logger.info('{}的请求方式不支持'.format(method))
                # print('{}的请求方式不支持'.format(method))
        except Exception as e:
            # print('请求报错了：{}'.format(e))
            my_logger.error('请求报错了：{}'.format(e))
            raise e
        my_logger.info(res.json())
        return res.json()


if __name__ == '__main__':
    url = "http://8.129.91.152:8766/futureloan/member/login"
    data = {"mobile_phone": "15512345678", "pwd": "test12345"}
    headers = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json"}
    res = HttpRequest().http_request('http://8.129.91.152:8766/futureloan/member/login', 'post', data=data,
                                     headers=headers)
    print(res)
