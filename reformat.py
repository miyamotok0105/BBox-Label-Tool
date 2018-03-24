# -*- coding: utf-8 -*-
#this script is covert form old format to new format.
#
#[new one]
#one line that class num and rect area.
#0 76 21 158 108
#[old one]
#twe line that rect of num and rect area.
#1
#76 21 158 108

import os
import sys
import math
import glob
import time
import json
import numpy as np

CLASS_NUM = 0
FOLDER = "002"

dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Labels", FOLDER, "*.txt")
for name in glob.glob(dir_path):
    new_line = []
    f = open(name)
    line = f.readline() 
    print("read line------->")
    while line:
        line = f.readline()
        if len(line) == 0:
            break
        # for debug
        # l = line.replace('\r\n','').replace('\n','').replace('\r','').split(" ")
        # print(l[0])
        # print(l[1])
        # print(l[2])
        # print(l[3])
        new_line.append(CLASS_NUM + " " + line)
    f.close

    os.remove(name)
    print("read new line------->")
    for nl in new_line:
        print(nl)

    print("write new line------->")
    for nl in new_line:
        print(nl)
        f = open(name,'a')
        f.write(nl)
        f.close()

