import os
import io
import re
import gc
import hashlib
import shutil
import time
import datetime


def get_file_list(root):
    file_list = [];
    print("Geting file list")
    count=0
    for root, dirs, files in os.walk(root):
        for f in files:
            count += 1
            path=root+os.path.sep+f
            file_list.append(path)
            if count%10000==0 :
                print("Find %d files"%(count))
    return file_list

def get_file_info(file_path):
    try:
        size=os.path.getsize(file_path)
        modify_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(os.path.getmtime(file_path)))
        last_access_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(os.path.getatime(file_path)))
        creat_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(os.path.getctime(file_path)))
        file_info=file_path+r'|'+str(size)+r'|'+creat_time+r'|'+modify_time+r'|'+last_access_time
    except:
        #pass
        file_info=r"0|0|0|0|0|################################"
    return file_info

def get_file_info_list(file_list):
    file_info_list=list()
    len_file_list=len(file_list)
    index=0
    for i in file_list:
        info=get_file_info(i)
        if info.__contains__("################################"):
            pass
        else:
            file_info_list.append(get_file_info(i))
            if index%1000==0:
                print(("%d\t%d\t%.3f/1000")%(len_file_list,index+1,((index+1)*1000)/len_file_list))
        index+=1
    return file_info_list

def get_file_info_list_write2file_per1000(file_path,file_list):
    file_info_list=list()
    len_file_list=len(file_list)
    index=0
    for i in file_list:
        file_info_list.append(get_file_info(i))


        if index%1000==0:
            append2file(file_path,file_info_list)
            del file_info_list
            file_info_list=list()
            print(("%d\t%d\t%.3f/1000")%(len_file_list,index+1,((index+1)*1000)/len_file_list))
        index+=1
    return file_info_list
