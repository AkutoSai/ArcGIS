#coding=utf-8
# -*- coding: UTF-8 -*-

import os
import arcpy
import copyfcbetweendirs
# Set source direction

dir_src = 'D:\py\inpath'

# Set target direction
dir_tar = 'D:\py\outpath'

# Set Data Set
ds = 'AD'

# Set Feature Class
fc = 'LCA'

copyfcbetweendirs.Do(dir_src,dir_tar,ds,fc)
