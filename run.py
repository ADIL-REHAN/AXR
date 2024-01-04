import os
try:
    os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
except:
    pass
import sys
import platform
import requests
_404_ = 'AXR.so'
_405_ = 'AXR_RN.so'
try:
    os.remove(_404_)
except:
    pass
try:
    os.remove(_405_)
except:
    pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile(_404_):
        try:
            os.system("clear")
            print("\033[1;32mDownloading Updated Version....!\033[1;37m")
            fumkyou = requests.get('https://github.com/ADIL-REHAN/XD/raw/main/AXR.cpython-311.so')
            with open(_404_, 'wb') as file:
                file.write(fumkyou.content)
            fumkyou2 = requests.get('https://github.com/ADIL-REHAN/XD/raw/main/AXR_RN.cpython-311.so')
            with open(_405_, 'wb') as file:
                file.write(fumkyou2.content)
            os.system("clear")
            print("[1] FILE CLONE ")
            print("[2] RANDOM CLONE")
            XD = input("Enter Your Choice : ")
            if XD == '1':
                import AXR
            elif XD == '2':
                import AXR_RN
            else:
                sys.exit("\033[1;31mInvalid choice. Exiting...\033[1;37m")
        except Exception as e:
            os.system("clear")
            print(f"\033[1;31mFailed to download updated version \033[1;31m:(\033[1;37m")
            sys.exit(1)
    else:
        sys.exit("\033[1;31mFILE Already Downloaded. Exiting...\033[1;37m")
else:
    sys.exit("\033[1;31mNOT SUPPORTED\033[1;37m")
