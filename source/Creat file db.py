#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      kcuwxl2
#
# Created:     13-12-2013
# Copyright:   (c) kcuwxl2 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import get_file_info_list as gfi
import read_write as rw
import time
import os

def get_roots(root_db):
    return rw.read2memory(root_db).split('\n')


def main():
    start_time=time.clock()
    root_db=r"dirs.txt"
    file_info_db=r"info_db.txt"
    if (os.path.exists(file_info_db)):
        os.remove(file_info_db)
    root_list=get_roots(root_db)
    for root in root_list:
        print(root)
        rw.append2file(file_info_db,gfi.get_file_list( root))

    end_time=time.clock()
    print("All time:%.3f"%(end_time-start_time))
    pass

if __name__ == '__main__':
    main()
