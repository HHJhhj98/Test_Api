# -*- coding：utf-8 -*-
# @Time ：2022/1/3 22:16
# @Authon :hhj
# @Annotation:
# @File : class_pandas.py


import pandas as pd


class Pandas:
    def reade_excel(self, file_name, sheet_name):
        df = pd.read_excel(file_name, sheet_name)
        test_data = []
        for i in df.index.values:  # 获取行号的索引，并对其进行遍历：
            # 根据i来获取每一行指定的数据 并利用to_dict转成字典
            row_data = df.loc[
                i, ['case_id', 'module', 'title', 'url', 'method', 'data', 'headers', 'expected']].to_dict()
            test_data.append(row_data)
        print("最终获取到的数据是：{0}".format(test_data))


if __name__ == '__main__':
    Pandas().reade_excel('test_data.xlsx','login')



