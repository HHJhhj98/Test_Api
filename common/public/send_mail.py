# -*- coding：utf-8 -*-
# @Time ：2022/1/10 23:01
# @Authon :hhj
# @Annotation:
# @File : send_mail.py

import yagmail


class SendMail:
    # 把测试报告作为附件发送到指定邮箱
    def send_mail(self, report):
        yag = yagmail.SMTP(user="3281502659@qq.com", password="pamhwavwqiofdbdf", host='smtp.qq.com', encoding='GBK')
        subject = "自动化测试报告"
        contents = "自动化用例已执行完毕，详细报告请查看附件"
        yag.send('2393022053@qq.com', subject, contents, report)
        print("邮件已经发送成功！")
