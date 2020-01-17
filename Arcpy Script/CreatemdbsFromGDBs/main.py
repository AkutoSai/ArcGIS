#coding = utf-8
# -*- coding: UTF-8 -*-

import os
import arcpy
from arcpy import env

import createmdbsfromgdbs


gdb_dir_in = u'E:/ZHX/ZHXIN'


mdb_dir_out = u'E:/ZHX/ZHXOUT'

print time.strftime("start:%Y/%m/%d:%H:%M:%S")
createmdbsfromgdbs.Do(gdb_dir_in,mdb_dir_out)
print time.strftime("done:%Y/%m/%d:%H:%M:%S")

