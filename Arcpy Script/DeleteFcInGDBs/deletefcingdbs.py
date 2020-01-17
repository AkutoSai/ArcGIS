#coding=utf-8
# -*- coding: UTF-8 -*-

import os
import arcpy


def Do():
    # Get the list of GDBs
    GDBs=os.listdir(indir)
    
    for thegdb in GDBs:
        fc_del = indir + os.sep + thegdb + os.sep + ds + os.sep + fc 
        print 'deleting ' + fc_del
        arcpy.Delete_management(fc_del) 
    print 'done'
if __name__=="__main__":
    print time.strftime("start:%Y/%m/%d:%H:%M:%S")
    Do(sys.argv[1],sys.argv[2]],sys.argv[3])
    print time.strftime("done:%Y/%m/%d:%H:%M:%S")
