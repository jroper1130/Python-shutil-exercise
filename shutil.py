# -*- coding: cp1252 -*-
'''
Python Drill: PyDrill_shutil_module_27_idle
Title: File Mover – Python 2.7 – IDLE
Scenario: Your employer wants a program to move all his .txt files from one
folder to another with the click of a click of a button. On your desktop make
2 new folders. Call one Folder A & the second Folder B. Create 4 random
.txt files & put them in Folder A.
Plan:
- Move the files from Folder A to Folder B.
- Print out each file path that got moved onto the shell.
- Upon viewing Folder A after the execution, the moved files should not be there.
=======================================================================================================================
'''
#drill5

import shutil
import os

def file_transfer(src, des):
    items = os.listdir(src)
    for file_name in items :
        if file_name.endswith(".txt"):
            shutil.move(os.path.join(src, file_name), des)

def main():
    src = ("C:/Users/warbe/Desktop/a/")
    des = ("C:/Users/warbe/Desktop/b/")
    file_transfer(src, des)

if __name__=='__main__':
    main()













