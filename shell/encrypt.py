#!/usr/bin/env python
#coding = utf-8

import os
import re

def encrypt(path):
    dirlist = os.listdir(path)
    pattern = re.compile(r'.*\.php')
    for i in dirlist:
        if os.path.isdir(path+'/'+i):
            encrypt(path+'/'+i)
        elif pattern.match(i):
            os.system("screw "+path+'/'+i)
            os.system("rm "+path+'/'+i+".screw")
    

if __name__ == '__main__':
    path = os.getcwd()
    encrypt(path+"/webapp")
