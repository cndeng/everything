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

file_db=r'info_db.txt'

def load_db():
    start_time=time.clock()

    file_list=rw.read2memory(file_db).split('\n')

    read_end_time=time.clock()
    print(" Time of loading db : %.2f (S)"%(read_end_time-start_time))

    return file_list

def search(file_list):

    key=input("Press your key word: ")
    search_start_time=time.clock()
    result_list=list()
    for f in file_list:
        base_name=f.replace( f.split('\\')[-1],'')
        if (base_name.__contains__(key)):
            result_list.append(f)
    search_end_time=time.clock()
    print("Search Time:%f , Find files:%d"%(search_end_time-search_start_time,len(result_list)))

    return result_list

def display(result_list):
    display_start_time=time.clock()
    count=0
    for r in result:
        print(count,r)
        count+=1
    display_end_time=time.clock()
    print("Display Time:%f , Find files:%d"%(search_end_time-search_start_time,display_end_time-display_start_time,count))

def open_file(result_list):
    num = int(input("File num to open:"))
    os.popen("explorer"+" "+result_list[num])

def main():
    search( load_db())

    input()
    pass
if __name__ == '__main__':
    main()
