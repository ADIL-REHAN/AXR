#coding=utf-8
import os, sys, platform
os.system('rm -rf AXS.so')
try:
    if sys.argv[1]=='update':
        os.system('rm -rf AXS.so')
except:
    pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('AXS.so'):
        os.system('curl -L https://github.com/ADIL-REHAN/XD/blob/main/AXS.cpython-311.so?raw=true -o AXS.so') 
        import AXS
    else:
        import AXS
elif bit == '32bit':
    exit("NOT SUPPORTED")
