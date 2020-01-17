#coding=utf-8
# -*- coding: UTF-8 -*-

import os
import sys
import time

import arcpy
from arcpy import env

import deletefcingdbs

# Set input direction
indir = 'D:\py\inpath'

# Set Data Set
ds = 'AD'

# Set Feature Class
fc = 'LCA'
if __name__=="__main__":
    print time.strftime("start:%Y/%m/%d:%H:%M:%S")
    deletefcingdbs.Do(indir,ds,fc)
    print time.strftime("done:%Y/%m/%d:%H:%M:%S")
