#coding = utf-8
# -*- coding: UTF-8 -*-

import os
import arcpy
from arcpy import env
import compactgdbs

gdb_dir_in = u'E:/ZHX/ZHXIN'

print time.strftime("start:%Y/%m/%d:%H:%M:%S")
compactgdbs.Do(gdb_dir_in)
print time.strftime("done:%Y/%m/%d:%H:%M:%S")