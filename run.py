#coding=utf-8
import os, sys, platform

os.system('rm -rf axr')

try:
    if sys.argv[1]=='update':
        os.system('rm -rf axr')
except:
    pass


bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('axr'):
        os.system('curl -L https://github.com/ADIL-REHAN/AXR/blob/main/axr?raw=true -o axr')
        os.system('chmod 777 axr ; ./axr')
    else:
        os.system('chmod 777 axr ; ./axr')
