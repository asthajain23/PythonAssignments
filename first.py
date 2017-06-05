#Write a python script for creating directory,displaying its contents:

import os
os.mkdir("demo1")
os.chdir("demo1")
os.system("touch file1.txt")
os.system("ls")

#Output
'''
python first.py
file1.txt '''