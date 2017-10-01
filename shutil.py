# -*- coding: cp1252 -*-
'''
Python Drill: PyDrill_shutil_module_27_idle
Title: File Mover – Python 2.7 – IDLE
Scenario: Your employer wants a program to move all his .txt files from one folder to another
with the click of a click of a button. On your desktop make 2 new folders. Call one Folder A &
the second Folder B. Create 4 random .txt files & put them in Folder A.
Plan:
- Move the files from Folder A to Folder B.
- Print out each file path that got moved onto the shell.
- Upon viewing Folder A after the execution, the moved files should not be there.
=======================================================================================================================
'''
#assuming files names are a and b, and txt docs are c, d, e, f.

import shutil

shutil.move('C:/Users/warbe/Desktop/a/c.txt','C:/Users/warbe/Desktop/b')
shutil.move('C:/Users/warbe/Desktop/a/d.txt','C:/Users/warbe/Desktop/b')
shutil.move('C:/Users/warbe/Desktop/a/e.txt','C:/Users/warbe/Desktop/b')
shutil.move('C:/Users/warbe/Desktop/a/f.txt','C:/Users/warbe/Desktop/b')



#havent turned in yet
#drill5
