import os
import sys
import time

import arcpy
from arcpy import env

import mergegdbs

#1
in_path = 'E:/ZHX/ZHXIN'

#2.1
out_path = 'E:/ZHX/ZHXOUT'

#2.2
out_gdb = 'output.gdb'

#3
fcs = [u'LRDL', u'BOUA5', 'LCA']

print time.strftime("start:%Y/%m/%d:%H:%M:%S")
mergegdbs.Do(in_path,out_path,out_gdb,fcs)
print time.strftime("done:%Y/%m/%d:%H:%M:%S")
test=raw_input("press any key to quit")
