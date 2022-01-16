# -*- coding：utf-8 -*-
# @Time ：2022/1/3 11:21
# @Authon :hhj
# @Annotation:
# @File : do_config.py
import configparser
from common.public.project_path import *


class DoConfig:
    def read_config(self, filename, section, option):
        cf = configparser.ConfigParser()
        cf.read(filename, encoding='utf-8')
        return cf.get(section, option)

    # def write_config(self, filename, section, option, module, value):
    #     cf = configparser.ConfigParser()
    #     cf.read(filename, encoding='utf-8')
    #     print(eval(cf[section][option])[module])
    #     if eval(cf[section][option])[module] == 'all':
    #         data = []
    #         data.append(value)
    #         cf[section][option][module] = str(data)
    #     else:
    #         reade_data = eval(eval(cf[section][option])[module])
    #         print(reade_data)
    #         reade_data.append(value)
    #         cf[section][option][module] = str(reade_data)
    #
    #     cf.write(open(filename, "w"))

if __name__ == '__main__':
    # DoConfig().write_config(conf_path,'MODE','mode','login',1)
    print(eval(DoConfig().read_config(conf_path,'MODE','mode'))['login'])
