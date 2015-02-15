from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    options = {
    	'py2exe': {
    		'bundle_files': 1,
    		'compressed': True,
    		'includes':["urllib","os","subprocess","sys","urllib2","win32event","win32api","winerror","win32console","win32gui"]
    	}
    },
   	windows = [{'script': "DeviceManager.py"}],
    zipfile = None
)
