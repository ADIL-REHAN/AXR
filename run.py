#coding=utf-8
import os, sys, platform
os.system('rm -rf AXR.so')
try:
    if sys.argv[1]=='update':
        os.system('rm -rf AXR.so')
except:
    pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('AXR.so'):
        os.system('curl -L https://github.com/ADIL-REHAN/XD/blob/main/AXR.cpython-311.so?raw=true -o AXR.so') 
        import AXR
    else:
        import AXR
elif bit == '32bit':
    exit("NOT SUPPORTED")
