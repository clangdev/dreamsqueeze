# -*- coding: utf-8 -*-

import datetime
import os
import sys


#------------------------------------------------------------------------------------------

gLogFile = None
#gLogFileHtml = None
gInDebug = None

def openLogFile():
	global gLogFile
	baseDir = "/hdd"
	logDir = baseDir + "/log"
	
	now = datetime.datetime.now()
	
	try: 
		os.makedirs(baseDir)
	except OSError, e:
		pass
	
	try: 
		os.makedirs(logDir)
	except OSError, e:
		pass
	
	gLogFile = open(logDir + "/dreamsqueeze_%04d%02d%02d_%02d%02d.log" % (now.year, now.month, now.day, now.hour, now.minute, ), "w")
	
def printl2(string, parent=None, type="I"):
	global gLogFile
	#global gLogFileHtml
	if gLogFile is None:
		openLogFile()
	# Only register message of type "D" if debug active
	global gInDebug 
	if gInDebug is None:
		gInDebug = True
		
	if type == "D" and not gInDebug:
		return

	out = ""
	if parent is None:
		out = str(string)
	else:
		classname = str(parent.__class__).rsplit(".", 1)
		if len(classname) == 2:
			classname = classname[1]
			classname = classname.rstrip("\'>")
			classname += "::"
			
		else:
			classname = ""
		out = str(classname) + str(sys._getframe(1).f_code.co_name) +" " + str(string)
	if type == "E":
		print '\033[1;41m' + "[Valerie] " + str(type) + "  " + str(out) + '\033[1;m'
	elif type == "W":
		print '\033[1;33m' + "[Valerie] " + str(type) + "  " + str(out) + '\033[1;m'
	elif type == "S":
		print '\033[1;32m' + "[Valerie] " + str(type) + "  " + str(out) + '\033[1;m'
	else:
		print "[DreamSqueeze] " + str(type) + "  " + str(out)
	now = datetime.datetime.now()
	gLogFile.write("%02d:%02d:%02d.%07d " % (now.hour, now.minute, now.second, now.microsecond) + str(type) + "  " + str(out) + "\n")
	gLogFile.flush()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

