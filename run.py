#WRITTEN BY REHAN
import os
try:os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
except:pass
import sys
import platform
import requests

_404_ = 'AXR.so'
try:os.remove(_404_)
except:pass

bit = platform.architecture()[0]

if bit == '64bit':
    if not os.path.isfile(_404_):
        try:
            os.system("clear")
            print("\033[1;32mDownloading Updated Version....!\033[1;37m")
            fumkyou = requests.get('https://github.com/ADIL-REHAN/XD/raw/main/AXR.cpython-311.so')
            with open(_404_, 'wb') as file:
                file.write(fumkyou.content)
            import AXR
        except Exception as e:
            os.system("clear")
            print(f"\033[1;31mFailed to download updated version \033[1;31m:(\033[1;37m")
            sys.exit(1)
    else:
        import AXR
else:
    sys.exit("\033[1;31mNOT SUPPORTED")
