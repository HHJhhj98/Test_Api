# -*- coding：utf-8 -*-
# @Time ：2022/1/3 22:59
# @Authon :hhj
# @Annotation:
# @File : read_data.py
from common.public.do_excel_old import DoExcel
from common.public.do_config import DoConfig


class ReadeData:

    def reade_data(self, config_file_name, config_mode, excel_file_name, sheetname):
        mode = DoConfig().read_config(config_file_name, 'MODE', config_mode)
        data = DoExcel().read_excel(excel_file_name, sheetname, mode)
        return data

if __name__ == '__main__':
    ReadeData().reade_data('..\\conf\\case.config', 'register_mode', '..\\..\\test_data\\test_data.xlsx', 'register')
