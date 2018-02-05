

import os

from os.path import isfile, join
from subprocess import call
import subprocess
from subprocess import PIPE,STDOUT
import re
import shlex

def getallvidfiles(absolute_target_path):
	os.chdir(absolute_target_path)
	currentpath = os.getcwd()
	allfiles = [f for f in os.listdir(currentpath) if isfile(join(currentpath,f))]
	allvidfiles = [f for f in allfiles if containsvidextension( os.path.splitext(join(currentpath,f))[1])]
	return allvidfiles

def containsvidextension(extension):
	
	if len(extension)==0:
		return False


	if extension[0]=='.':
		extension=extension[1:]
	# print "extension"+extension

	availableexts = ["mp4","avi"]
	if extension in availableexts:
		# print "returning true"
		return True
	else:
		# print "returning false"
		return False

def contain_given_exts(testext,extlist):
	# print testext
	# print extlist
	if len(testext)==0:
		return False

	if testext[0]=='.':
		testext = testext[1:]

	if testext in extlist:
		return True
	else:
		return False


def getduration(videofile):
	cmdstr = "ffprobe -i " + videofile + " -show_entries format=duration -v quiet -of csv=\"p=0\""
	# cmdstr = "ffprobe -i " + videofile + " -show_entries format=duration -v quiet -of csv"
	# output1 = call(cmdstr,shell=True)
	# print "shlex result="
	# print shlex.split(cmdstr)
	process = subprocess.Popen(shlex.split(cmdstr), stdout = subprocess.PIPE)

	stdout = process.communicate()[0]
	# print "stdout="+stdout

	p = re.compile("(.+)\.")
	m = p.findall(stdout)
	# if m:
		# print m

	totalsecondlength=int(m[0])
	return totalsecondlength


def getallimagefiles(target_abs_path):
	
	allfiles = [f for f in os.listdir(target_abs_path) if os.path.isfile(f)]
	# print allfiles
	filterimg_exts = ["jpg","png"]
	imgfiles = [f for f in allfiles if contain_given_exts(os.path.splitext(join(target_abs_path,f))[1],filterimg_exts)]
	# print imgfiles
	return imgfiles



def create_zip(outputzipfilename, filelisttozip):
	filelist_str = ""
	for f in filelisttozip:
		filelist_str = filelist_str + f + " "
	cmdstr= "zip "+outputzipfilename+" "+ filelist_str
	
	process = subprocess.Popen(shlex.split(cmdstr), stdout = subprocess.PIPE)
	stdout = process.communicate()[0]



