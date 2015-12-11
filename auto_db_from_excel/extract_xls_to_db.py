#!/usr/bin/env python
#
# Copyright (C) 2015 funtv
#
# Any question please contect chenhai@fun.tv

import os
import argparse
import xdrlib ,sys
import xlrd
import sqlite3
import gl

from public import switch

DEBUG = 0

def open_excel(file= u'adjust.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)

def excel_table_byname(file= u'adjust.xls', col_name_index=0, by_name=u'Sheet1'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    return table

def fill_global_data(table):
    nrows = table.nrows
    ncols = table.ncols
    for rownum in range(1,nrows):
        count = 0 # count the row number
        row = table.row_values(rownum)
        for i in row:
            for case in switch(i):
                if case(gl.COOL_CHAR):
                    gl.COOL_COL = count
                    break
                if case(gl.NORMAL_CHAR):
                    gl.NORMAL_COL = count
                    break
                if case(gl.WARM_CHAR):
                    gl.WARM_COL = count
                    break
                if case(gl.BRIGHTNESS_CHAR):
                    gl.BRIGHTNESS_COL = count
                    break
                if case(gl.CONTRAST_CHAR):
                    gl.CONTRAST_COL = count
                    break
                if case(gl.SATURATION_CHAR):
                    gl.SATURATION_COL = count
                    break
                if case(gl.HUE_CHAR):
                    gl.HUE_COL = count
                    break
                if case(gl.SHARPNESS_CHAR):
                    gl.SHARPNESS_COL = count
                    break
            count +=1


def organizing_data(table):
    nrows = table.nrows
    ncols = table.ncols
    part = 0

    for rownum in range(1,nrows):
        row = table.row_values(rownum)
       # print row
        for i in row:
            if (i == gl.GAIN_R_CHAR):
                fill_color_dict(row, i)
            if (i == gl.GAIN_G_CHAR):
                fill_color_dict(row, i)
            if (i == gl.GAIN_B_CHAR):
                fill_color_dict(row, i)
            if (i == gl.OFFSET_R_CHAR):
                fill_offset_dict(row, i)
            if (i == gl.OFFSET_G_CHAR):
                fill_offset_dict(row, i)
            if (i == gl.OFFSET_B_CHAR):
                fill_offset_dict(row, i)

            ## part 1
            if (i == gl.SRC_CHANNEL_DIG):
                part = 1
            if (i == gl.SRC_CHANNEL_TV):
                part = 2
            if (i == gl.SRC_CHANNEL_PC):
                part = 3


            if (i == 0.0) and (part == 1):
                fill_nonliner_dig_dict(row, '0')
            if (i == 25.0) and (part == 1):
                fill_nonliner_dig_dict(row, '25')
            if (i == 50.0) and (part == 1):
                fill_nonliner_dig_dict(row, '50')
            if (i == 75.0) and (part == 1):
                fill_nonliner_dig_dict(row, '75')
            if (i == 100.0) and (part == 1):
                fill_nonliner_dig_dict(row, '100')
                            
            if (i == 0.0) and (part == 2):
                fill_nonliner_tv_dict(row, '0')
            if (i == 25.0) and (part == 2):
                fill_nonliner_tv_dict(row, '25')
            if (i == 50.0) and (part == 2):
                fill_nonliner_tv_dict(row, '50')
            if (i == 75.0) and (part == 2):
                fill_nonliner_tv_dict(row, '75')
            if (i == 100.0) and (part == 2):
                fill_nonliner_tv_dict(row, '100')

            if (i == 0.0) and (part == 3):
                fill_nonliner_pc_dict(row, '0')
            if (i == 25.0) and (part == 3):
                fill_nonliner_pc_dict(row, '25')
            if (i == 50.0) and (part == 3):
                fill_nonliner_pc_dict(row, '50')
            if (i == 75.0) and (part == 3):
                fill_nonliner_pc_dict(row, '75')
            if (i == 100.0) and (part == 3):
                fill_nonliner_pc_dict(row, '100')

def get_conn(path):
    '''Get the particular database handle'''
    if os.path.exists(path) and os.path.isfile(path):
        conn = sqlite3.connect(path)
    else:
        conn = None
    return conn

def get_cursor(conn):
    '''Get the cursor of db we connected'''
    if conn is not None:
        cur = conn.cursor()
    else:
        print "The db cant be connected, please check!"
        exit()
    return cur

def update_db(file=u'factory.db'):
    conn = get_conn(file)
    cur = get_cursor(conn)

    #update  tbl_FactoryColorTempEx table
    ## cool channel
    cur.execute('UPDATE tbl_FactoryColorTempEx SET u16RedGain=? WHERE ColorTemperatureID LIKE ?;', (gl.DICT_GAIN_COOL[gl.GAIN_R_CHAR]*8, gl.COOL))
    cur.execute('UPDATE tbl_FactoryColorTempEx SET u16GreenGain=? WHERE ColorTemperatureID LIKE ?;', (gl.DICT_GAIN_COOL[gl.GAIN_G_CHAR]*8, gl.COOL))
    cur.execute('UPDATE tbl_FactoryColorTempEx SET u16BlueGain=? WHERE ColorTemperatureID LIKE ?;', (gl.DICT_GAIN_COOL[gl.GAIN_B_CHAR]*8, gl.COOL))
#    cur.execute('UPDATE tbl_FactoryColorTempEx SET u16RedGain=? WHERE _rowid_=?;', (gl.DICT_GAIN_COOL[gl.GAIN_B_CHAR]*8, 1))
    ## normal channel
    cur.execute('UPDATE tbl_FactoryColorTempEx SET u16RedGain=? WHERE ColorTemperatureID LIKE ?;', (gl.DICT_GAIN_NORMAL[gl.GAIN_R_CHAR]*8, gl.NORMAL))
    cur.execute('UPDATE tbl_FactoryColorTempEx SET u16GreenGain=? WHERE ColorTemperatureID LIKE ?;', (gl.DICT_GAIN_NORMAL[gl.GAIN_G_CHAR]*8, gl.NORMAL))
    cur.execute('UPDATE tbl_FactoryColorTempEx SET u16BlueGain=? WHERE ColorTemperatureID LIKE ?;', (gl.DICT_GAIN_NORMAL[gl.GAIN_B_CHAR]*8, gl.NORMAL))
    ## warm channel
    cur.execute('UPDATE tbl_FactoryColorTempEx SET u16RedGain=? WHERE ColorTemperatureID LIKE ?;', (gl.DICT_GAIN_WARM[gl.GAIN_R_CHAR]*8, gl.WARM))
    cur.execute('UPDATE tbl_FactoryColorTempEx SET u16GreenGain=? WHERE ColorTemperatureID LIKE ?;', (gl.DICT_GAIN_WARM[gl.GAIN_G_CHAR]*8, gl.WARM))
    cur.execute('UPDATE tbl_FactoryColorTempEx SET u16BlueGain=? WHERE ColorTemperatureID LIKE ?;', (gl.DICT_GAIN_WARM[gl.GAIN_B_CHAR]*8, gl.WARM))

    # offset cool
    cur.execute('UPDATE tbl_FactoryColorTempEx SET u16RedOffset=? WHERE ColorTemperatureID LIKE ?;', (gl.DICT_OFFSET_COOL[gl.OFFSET_R_CHAR], gl.COOL))
    cur.execute('UPDATE tbl_FactoryColorTempEx SET u16GreenOffset=? WHERE ColorTemperatureID LIKE ?;', (gl.DICT_OFFSET_COOL[gl.OFFSET_G_CHAR], gl.COOL))
    cur.execute('UPDATE tbl_FactoryColorTempEx SET u16BlueOffset=? WHERE ColorTemperatureID LIKE ?;', (gl.DICT_OFFSET_COOL[gl.OFFSET_B_CHAR], gl.COOL))
    # offset normal
    cur.execute('UPDATE tbl_FactoryColorTempEx SET u16RedOffset=? WHERE ColorTemperatureID LIKE ?;', (gl.DICT_OFFSET_NORMAL[gl.OFFSET_R_CHAR], gl.NORMAL))
    cur.execute('UPDATE tbl_FactoryColorTempEx SET u16GreenOffset=? WHERE ColorTemperatureID LIKE ?;', (gl.DICT_OFFSET_NORMAL[gl.OFFSET_G_CHAR], gl.NORMAL))
    cur.execute('UPDATE tbl_FactoryColorTempEx SET u16BlueOffset=? WHERE ColorTemperatureID LIKE ?;', (gl.DICT_OFFSET_NORMAL[gl.OFFSET_B_CHAR], gl.NORMAL))
    # offset warm
    cur.execute('UPDATE tbl_FactoryColorTempEx SET u16RedOffset=? WHERE ColorTemperatureID LIKE ?;', (gl.DICT_OFFSET_WARM[gl.OFFSET_R_CHAR], gl.WARM))
    cur.execute('UPDATE tbl_FactoryColorTempEx SET u16GreenOffset=? WHERE ColorTemperatureID LIKE ?;', (gl.DICT_OFFSET_WARM[gl.OFFSET_G_CHAR], gl.WARM))
    cur.execute('UPDATE tbl_FactoryColorTempEx SET u16BlueOffset=? WHERE ColorTemperatureID LIKE ?;', (gl.DICT_OFFSET_WARM[gl.OFFSET_B_CHAR], gl.WARM))


    #update  tbl_NonLinearAdjust
    if gl.DICT_DIG_BRIGHT['0'] is not '':
        cur.execute('UPDATE tbl_NonLinearAdjust SET u8OSD_V0=? WHERE CurveTypeIndex LIKE ?;', (gl.DICT_DIG_BRIGHT['0'], gl.BRIGHTNESS))
    if gl.DICT_DIG_BRIGHT['25'] is not '':
        cur.execute('UPDATE tbl_NonLinearAdjust SET u8OSD_V25=? WHERE CurveTypeIndex LIKE ?;', (gl.DICT_DIG_BRIGHT['25'], gl.BRIGHTNESS))
    if gl.DICT_DIG_BRIGHT['50'] is not '':
        cur.execute('UPDATE tbl_NonLinearAdjust SET u8OSD_V50=? WHERE CurveTypeIndex LIKE ?;', (gl.DICT_DIG_BRIGHT['50'], gl.BRIGHTNESS))
    if gl.DICT_DIG_BRIGHT['75'] is not '':
        cur.execute('UPDATE tbl_NonLinearAdjust SET u8OSD_V75=? WHERE CurveTypeIndex LIKE ?;', (gl.DICT_DIG_BRIGHT['75'], gl.BRIGHTNESS))
    if gl.DICT_DIG_BRIGHT['100'] is not '':
        cur.execute('UPDATE tbl_NonLinearAdjust SET u8OSD_V100=? WHERE CurveTypeIndex LIKE ?;', (gl.DICT_DIG_BRIGHT['100'], gl.BRIGHTNESS))

    if gl.DICT_DIG_CONTRAST['0'] is not '':
        cur.execute('UPDATE tbl_NonLinearAdjust SET u8OSD_V0=? WHERE CurveTypeIndex LIKE ?;', (gl.DICT_DIG_CONTRAST['0'], gl.CONTRAST))
    if gl.DICT_DIG_CONTRAST['25'] is not '':
        cur.execute('UPDATE tbl_NonLinearAdjust SET u8OSD_V25=? WHERE CurveTypeIndex LIKE ?;', (gl.DICT_DIG_CONTRAST['25'], gl.CONTRAST))
    if gl.DICT_DIG_CONTRAST['50'] is not '':
        cur.execute('UPDATE tbl_NonLinearAdjust SET u8OSD_V50=? WHERE CurveTypeIndex LIKE ?;', (gl.DICT_DIG_CONTRAST['50'], gl.CONTRAST))
    if gl.DICT_DIG_CONTRAST['75'] is not '':
        cur.execute('UPDATE tbl_NonLinearAdjust SET u8OSD_V75=? WHERE CurveTypeIndex LIKE ?;', (gl.DICT_DIG_CONTRAST['75'], gl.CONTRAST))
    if gl.DICT_DIG_CONTRAST['100'] is not '':
        cur.execute('UPDATE tbl_NonLinearAdjust SET u8OSD_V100=? WHERE CurveTypeIndex LIKE ?;', (gl.DICT_DIG_CONTRAST['100'], gl.CONTRAST))

    if gl.DICT_DIG_SATURATION['0'] is not '':
        cur.execute('UPDATE tbl_NonLinearAdjust SET u8OSD_V0=? WHERE CurveTypeIndex LIKE ?;', (gl.DICT_DIG_SATURATION['0'], gl.SATURATION))
    if gl.DICT_DIG_SATURATION['25'] is not '':
        cur.execute('UPDATE tbl_NonLinearAdjust SET u8OSD_V25=? WHERE CurveTypeIndex LIKE ?;', (gl.DICT_DIG_SATURATION['25'], gl.SATURATION))
    if gl.DICT_DIG_SATURATION['50'] is not '':
        cur.execute('UPDATE tbl_NonLinearAdjust SET u8OSD_V50=? WHERE CurveTypeIndex LIKE ?;', (gl.DICT_DIG_SATURATION['50'], gl.SATURATION))
    if gl.DICT_DIG_SATURATION['75'] is not '':
        cur.execute('UPDATE tbl_NonLinearAdjust SET u8OSD_V75=? WHERE CurveTypeIndex LIKE ?;', (gl.DICT_DIG_SATURATION['75'], gl.SATURATION))
    if gl.DICT_DIG_SATURATION['100'] is not '':
        cur.execute('UPDATE tbl_NonLinearAdjust SET u8OSD_V100=? WHERE CurveTypeIndex LIKE ?;', (gl.DICT_DIG_SATURATION['100'], gl.SATURATION))

    if gl.DICT_DIG_SHARP['0'] is not '':
        cur.execute('UPDATE tbl_NonLinearAdjust SET u8OSD_V0=? WHERE CurveTypeIndex LIKE ?;', (gl.DICT_DIG_SHARP['0'], gl.SHARPNESS))
    if gl.DICT_DIG_SHARP['25'] is not '':
        cur.execute('UPDATE tbl_NonLinearAdjust SET u8OSD_V25=? WHERE CurveTypeIndex LIKE ?;', (gl.DICT_DIG_SHARP['25'], gl.SHARPNESS))
    if gl.DICT_DIG_SHARP['50'] is not '':
        cur.execute('UPDATE tbl_NonLinearAdjust SET u8OSD_V50=? WHERE CurveTypeIndex LIKE ?;', (gl.DICT_DIG_SHARP['50'], gl.SHARPNESS))
    if gl.DICT_DIG_SHARP['75'] is not '':
        cur.execute('UPDATE tbl_NonLinearAdjust SET u8OSD_V75=? WHERE CurveTypeIndex LIKE ?;', (gl.DICT_DIG_SHARP['75'], gl.SHARPNESS))
    if gl.DICT_DIG_SHARP['100'] is not '':
        cur.execute('UPDATE tbl_NonLinearAdjust SET u8OSD_V100=? WHERE CurveTypeIndex LIKE ?;', (gl.DICT_DIG_SHARP['100'], gl.SHARPNESS))

    if gl.DICT_DIG_HUE['0'] is not '':
        cur.execute('UPDATE tbl_NonLinearAdjust SET u8OSD_V0=? WHERE CurveTypeIndex LIKE ?;', (gl.DICT_DIG_HUE['0'], gl.HUE))
    if gl.DICT_DIG_HUE['25'] is not '':
        cur.execute('UPDATE tbl_NonLinearAdjust SET u8OSD_V25=? WHERE CurveTypeIndex LIKE ?;', (gl.DICT_DIG_HUE['25'], gl.HUE))
    if gl.DICT_DIG_HUE['50'] is not '':
        cur.execute('UPDATE tbl_NonLinearAdjust SET u8OSD_V50=? WHERE CurveTypeIndex LIKE ?;', (gl.DICT_DIG_HUE['50'], gl.HUE))
    if gl.DICT_DIG_HUE['75'] is not '':
        cur.execute('UPDATE tbl_NonLinearAdjust SET u8OSD_V75=? WHERE CurveTypeIndex LIKE ?;', (gl.DICT_DIG_HUE['75'], gl.HUE))
    if gl.DICT_DIG_HUE['100'] is not '':
        cur.execute('UPDATE tbl_NonLinearAdjust SET u8OSD_V100=? WHERE CurveTypeIndex LIKE ?;', (gl.DICT_DIG_HUE['100'], gl.HUE))

    conn.commit()
    conn.close()
    ##update tbl_NonLinearAdjust table
    

def fill_color_dict(row, dict_key):
    for count in range(len(row)):
        for case in switch(count):
            if case(gl.COOL_COL): 
                gl.DICT_GAIN_COOL[dict_key] = row[count]
                break
            if case(gl.NORMAL_COL):
                gl.DICT_GAIN_NORMAL[dict_key] = row[count]
                break
            if case(gl.WARM_COL):
                gl.DICT_GAIN_WARM[dict_key] = row[count]
                break

def fill_offset_dict(row, dict_key):
    for count in range(len(row)):
        for case in switch(count):
            if case(gl.COOL_COL): 
                gl.DICT_OFFSET_COOL[dict_key] = row[count]
                break
            if case(gl.NORMAL_COL):
                gl.DICT_OFFSET_NORMAL[dict_key] = row[count]
                break
            if case(gl.WARM_COL):
                gl.DICT_OFFSET_WARM[dict_key] = row[count]
                break

def fill_nonliner_dig_dict(row, dict_key):
    for count in range(len(row)):
        for case in switch(count):
            if case(gl.BRIGHTNESS_COL):
                gl.DICT_DIG_BRIGHT[dict_key] = row[count]
                break
            if case(gl.CONTRAST_COL):
                gl.DICT_DIG_CONTRAST[dict_key] = row[count]
                break
            if case(gl.SATURATION_COL):
                gl.DICT_DIG_SATURATION[dict_key] = row[count]
                break
            if case(gl.HUE_COL):
                gl.DICT_DIG_HUE[dict_key] = row[count]
                break
            if case(gl.SHARPNESS_COL):
                gl.DICT_DIG_SHARP[dict_key] = row[count]
                break

def fill_nonliner_tv_dict(row, dict_key):
    for count in range(len(row)):
        for case in switch(count):
            if case(gl.BRIGHTNESS_COL):
                gl.DICT_TV_BRIGHT[dict_key] = row[count]
                break
            if case(gl.CONTRAST_COL):
                gl.DICT_TV_CONTRAST[dict_key] = row[count]
                break
            if case(gl.SATURATION_COL):
                gl.DICT_TV_SATURATION[dict_key] = row[count]
                break
            if case(gl.HUE_COL):
                gl.DICT_TV_HUE[dict_key] = row[count]
                break
            if case(gl.SHARPNESS_COL):
                gl.DICT_TV_SHARP[dict_key] = row[count]
                break

def fill_nonliner_pc_dict(row, dict_key):
    for count in range(len(row)):
        for case in switch(count):
            if case(gl.BRIGHTNESS_COL):
                gl.DICT_PC_BRIGHT[dict_key] = row[count]
                break
            if case(gl.CONTRAST_COL):
                gl.DICT_PC_CONTRAST[dict_key] = row[count]
                break
            if case(gl.SATURATION_COL):
                gl.DICT_PC_SATURATION[dict_key] = row[count]
                break
            if case(gl.HUE_COL):
                gl.DICT_PC_HUE[dict_key] = row[count]
                break
            if case(gl.SHARPNESS_COL):
                gl.DICT_PC_SHARP[dict_key] = row[count]
                break

def printout_info():
    if (DEBUG == 1):
        print(gl.COOL_COL, gl.NORMAL_COL, gl.WARM_COL, gl.BRIGHTNESS_COL, gl.CONTRAST_COL, gl.SATURATION_COL, gl.HUE_COL, gl.SHARPNESS_COL)

        print gl.DICT_GAIN_COOL
        print gl.DICT_GAIN_NORMAL
        print gl.DICT_GAIN_WARM
        print gl.DICT_OFFSET_COOL
        print gl.DICT_OFFSET_NORMAL
        print gl.DICT_OFFSET_WARM
       
        print gl.DICT_DIG_BRIGHT
        print gl.DICT_DIG_CONTRAST
        print gl.DICT_DIG_SATURATION
        print gl.DICT_DIG_HUE
        print gl.DICT_DIG_SHARP

        print gl.DICT_TV_BRIGHT
        print gl.DICT_TV_CONTRAST
        print gl.DICT_TV_SATURATION
        print gl.DICT_TV_HUE
        print gl.DICT_TV_SHARP

def main(argv):

    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--file',help='ecxcel to be extracted')
    parser.add_argument('-d','--dstdb',help='database to be update')
    parser.add_argument('-v','--version',action='version',version='%(prog)s 1.0',help='print version')

    args=parser.parse_args()

    tables = excel_table_byname(args.file)

    fill_global_data(tables)
    organizing_data(tables)
    printout_info()
    update_db(args.dstdb)


if __name__=="__main__":
    main(sys.argv[1:])
