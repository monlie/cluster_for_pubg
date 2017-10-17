# -*- coding: utf-8 -*-

import xlrd
import numpy as np

#打开Excel文档
def open_exl(address, idx):
    data = xlrd.open_workbook(address)
    table = data.sheets()[idx]
    rows = table.nrows
    ct_data = []
    for row in range(rows):
        ct_data.append(table.row_values(row))
    return np.array(ct_data)

#将矩阵保存为csv文件
def create_csv(data, count):
    np.savetxt('%d_img.csv' % count, data, delimiter = ',')
        
if __name__ == '__main__':
    ct_data = open_exl('A.xls', 0)

