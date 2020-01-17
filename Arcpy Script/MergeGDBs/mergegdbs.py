#coding = utf-8
# -*- coding: UTF-8 -*-

import os
import arcpy
from arcpy import env

def delete_file_folder(src):  
    '''delete files and folders''' 
    if os.path.isfile(src):  
        try:  
            os.remove(src)  
        except:  
            pass 
    elif os.path.isdir(src):  
        for item in os.listdir(src):  
            itemsrc=os.path.join(src,item)  
            delete_file_folder(itemsrc)  
        try: 
            os.rmdir(src)  
        except: 
            pass 

def  Do(in_path,out_path,out_gdb,fcs):
   
    env.workspace = in_path
    gdblist = arcpy.ListWorkspaces()
       
    outGDBpath = os.path.join(out_path,out_gdb)
        
    if os.path.exists(outGDBpath):
        delete_file_folder(outGDBpath)
       
    arcpy.CreateFileGDB_management(out_path,out_gdb)
    
    for fc in fcs:
        
        fc_out = outGDBpath + os.sep + fc
        
        fclist = []
        fc_cnt1 = 0
        
        for gdb in gdblist:
            if not gdb[-4:] in [".gdb"]:
                continue
            
            fc_from = gdb +os.sep + fc
            if arcpy.Exists(fc_from):
                
                fclist.append(fc_from)
                
                fc_count = int(arcpy.GetCount_management(fc_from).getOutput(0))
                fc_cnt1 = fc_cnt1 + fc_count
                print fc_from + ': ' + str(fc_count)
            else:
                print fc_from + ' is missing'
        
        print str(fc_cnt1) + ' fcs input'
        
        arcpy.Merge_management(fclist,fc_out)
        
        fc_cnt2 = int(arcpy.GetCount_management(fc_out).getOutput(0))
        print str(fc_cnt2) + ' fcs output'
if __name__=="__main__":
    print time.strftime("start:%Y/%m/%d:%H:%M:%S")
    Do(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
    print time.strftime("done:%Y/%m/%d:%H:%M:%S")
