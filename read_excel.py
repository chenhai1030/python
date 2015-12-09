#!/usr/bin/env python
#
# Copyright (C) 2015 funtv
#
# Any question please contect chenhai@fun.tv

import xdrlib ,sys
import xlrd


def open_excel(file= 'adjust.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)

def excel_table_byname(file= 'adjust.xls', col_name_index=0, by_name=u'Sheet1'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows
    ncols = table.ncols
    col_names = table.row_values(col_name_index)
#    list = []
#    for rownum in range(1,nrows):
#        row = table.row_values(rownum)
#        #print row
#        if row:
#            app = {}
#            for i in range(len(col_names)):
#                app[col_names[i]] = row[i]
#                print row[i]
#                list.append(app)
#    return list
    for rownum in range(1,nrows):
        row = table.row_values(rownum)
        print row
    
    return table

def main():
    tables = excel_table_byname()
#    for row in tables:
#        print row


if __name__=="__main__":
    main()
