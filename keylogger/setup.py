from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    options = {
    	'py2exe': {
    		'bundle_files': 1,
    		'compressed': True,
    		'includes':["pythoncom","pyHook","os","sys","threading","urllib","urllib2","datetime","time","win32event","win32api","winerror"]
    	}
    },
   	windows = [{'script': "VGAdriver.py"}],
    zipfile = None
)