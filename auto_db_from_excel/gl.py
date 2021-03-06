#!/usr/bin/env python
# global variable define

## tab name
COLOR_TEMPRATURE_TABLE = 'tbl_FactoryColorTempEx'
NON_LINEAR_TABLE = 'tbl_NonLinearAdjust'
DICT_DB_TABLE = {'db_table1':COLOR_TEMPRATURE_TABLE, 'db_table2':0}

## define 
COOL = 0
NORMAL = 1
WARM = 2

BRIGHTNESS = 1
CONTRAST = 2
SATURATION = 3
SHARPNESS = 4
HUE = 5


############################################################
## column label
COOL_COL = 0
NORMAL_COL = 0
WARM_COL = 0

BRIGHTNESS_COL = 0
CONTRAST_COL = 0
SATURATION_COL = 0
HUE_COL = 0
SHARPNESS_COL = 0

## 
COOL_CHAR = u'Cool'
NORMAL_CHAR = u'Normal'
WARM_CHAR = u'Warm'

BRIGHTNESS_CHAR = u'Brightness'
CONTRAST_CHAR = u'Contrast'
SATURATION_CHAR = u'Saturation'
HUE_CHAR = u'Hue'
SHARPNESS_CHAR = u'Sharpness'

GAIN_R_CHAR = u'R-GAIN'
GAIN_G_CHAR = u'G-GAIN'
GAIN_B_CHAR = u'B-GAIN'

OFFSET_R_CHAR = u'R-OFFSET'
OFFSET_G_CHAR = u'G-OFFSET'
OFFSET_B_CHAR = u'B-OFFSET'

SRC_CHANNEL_DIG = u'HDMI/YPBPR/USB'
SRC_CHANNEL_TV = u'TV/AV'
SRC_CHANNEL_PC = u'PC'

#color dict
DICT_GAIN_COOL = {'name':COOL_CHAR, GAIN_R_CHAR:0, GAIN_G_CHAR:0, GAIN_B_CHAR:0}
DICT_GAIN_NORMAL = {'name':NORMAL_CHAR, GAIN_R_CHAR:0, GAIN_G_CHAR:0 , GAIN_B_CHAR:0}
DICT_GAIN_WARM = {'name':WARM_CHAR, GAIN_R_CHAR:0, GAIN_G_CHAR:0, GAIN_B_CHAR:0}
DICT_OFFSET_COOL = {'name':COOL_CHAR, OFFSET_R_CHAR:0, OFFSET_G_CHAR:0, OFFSET_B_CHAR:0}
DICT_OFFSET_NORMAL = {'name':NORMAL_CHAR, OFFSET_R_CHAR:0, OFFSET_G_CHAR:0, OFFSET_B_CHAR:0}
DICT_OFFSET_WARM = {'name':WARM_CHAR, OFFSET_R_CHAR:0, OFFSET_G_CHAR:0, OFFSET_B_CHAR:0}

##nonliner dict 
DICT_DIG_BRIGHT = {'name':BRIGHTNESS_CHAR, '0':0, '25':0, '50':0, '75':0, '100':0}
DICT_DIG_CONTRAST = {'name':CONTRAST_CHAR, '0':0, '25':0, '50':0, '75':0, '100':0}
DICT_DIG_SATURATION = {'name':SATURATION_CHAR, '0':0, '25':0, '50':0, '75':0, '100':0}
DICT_DIG_HUE = {'name':HUE_CHAR, '0':0, '25':0, '50':0, '75':0, '100':0}
DICT_DIG_SHARP = {'name':SHARPNESS_CHAR, '0':0, '25':0, '50':0, '75':0, '100':0}

DICT_TV_BRIGHT = {'name':BRIGHTNESS_CHAR, '0':0, '25':0, '50':0, '75':0, '100':0}
DICT_TV_CONTRAST = {'name':CONTRAST_CHAR, '0':0, '25':0, '50':0, '75':0, '100':0}
DICT_TV_SATURATION = {'name':SATURATION_CHAR, '0':0, '25':0, '50':0, '75':0, '100':0}
DICT_TV_HUE = {'name':HUE_CHAR, '0':0, '25':0, '50':0, '75':0, '100':0}
DICT_TV_SHARP = {'name':SHARPNESS_CHAR, '0':0, '25':0, '50':0, '75':0, '100':0}

DICT_PC_BRIGHT = {'name':BRIGHTNESS_CHAR, '0':0, '25':0, '50':0, '75':0, '100':0}
DICT_PC_CONTRAST = {'name':CONTRAST_CHAR, '0':0, '25':0, '50':0, '75':0, '100':0}
DICT_PC_SATURATION = {'name':SATURATION_CHAR, '0':0, '25':0, '50':0, '75':0, '100':0}
DICT_PC_HUE = {'name':HUE_CHAR, '0':0, '25':0, '50':0, '75':0, '100':0}
DICT_PC_SHARP = {'name':SHARPNESS_CHAR, '0':0, '25':0, '50':0, '75':0, '100':0}
