#-------------------------------------------------------------------------------
# Name:        Search_file
# Purpose:
#
# Author:      John
#
# Created:     11/01/2014
# Copyright:   (c) John 2014
# Licence:     <GPL3>
#-------------------------------------------------------------------------------
import read_write as rw
import time
import os

def main():

    start_time=time.clock()

    file_db=r'info_db.txt'
    file_list=rw.read2memory(file_db).split('\n')

    key=input("Press your key word: ")
    count=0
    result=list()
    for f in file_list:
        base_name=f.split('\\')[-1]
        if (base_name.__contains__(key)):
            result.append(f)
            print("%d\t%s"%(count,f))
            count+=1
            pass
    pass
    end_time=time.clock()

    print("Time:%d Find:%d"%(end_time-start_time,count))
    num = int(input("File num to open:"))
    os.popen("explorer"+" "+result[num])
if __name__ == '__main__':
    main()
