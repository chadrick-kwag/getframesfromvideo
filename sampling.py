from subprocess import call
import subprocess
from subprocess import PIPE,STDOUT
import sys
import re
import shlex
import os
import shutil

try:
    from subprocess import DEVNULL # py3k
except ImportError:
    import os
    DEVNULL = open(os.devnull, 'wb')


INTERVAL_SECOND=1


def mainjob(videofile, specified_outputdir=None):
	# DEVNULL = open(os.devnull,'wb')
	# call(['ffmpeg','-i',videofile,'\|','grep','\"Duration\"'])
	# cmdstr = "ffmpeg -i " + videofile + " | grep Duration"
	
	videofilename = os.path.splitext(videofile)[0]
	cmdstr = "ffprobe -i " + videofile + " -show_entries format=duration -v quiet -of csv=\"p=0\""
	# cmdstr = "ffprobe -i " + videofile + " -show_entries format=duration -v quiet -of csv"
	# output1 = call(cmdstr,shell=True)
	print "shlex result="
	print shlex.split(cmdstr)
	process = subprocess.Popen(shlex.split(cmdstr), stdout = subprocess.PIPE)

	stdout = process.communicate()[0]
	print "stdout="+stdout


	outputdirpath=""
	# create output dir
	if specified_outputdir is None:
		# when specified_outputdir is not specified, then automatically create a output dir 
		# with the video file's name
		cwd = os.getcwd()
		outputdirpath = cwd+"/"+videofilename
		print "otuputdirpath="+outputdirpath
		directory = os.path.dirname(outputdirpath)

		if not os.path.isdir(outputdirpath):
			print "dir does not exist. creating one."
			os.makedirs(outputdirpath)
		else:
			print "dir exists"
			# delete the whole dir. for clean start
			shutil.rmtree(outputdirpath)
			os.makedirs(outputdirpath)
		specified_outputdir = videofilename
	else:
		# if specified_outputdir is specified, it is likely that the output dir is already created.
		outputdirpath=os.path.join(os.getcwd(),specified_outputdir)

	
	p = re.compile("(.+)\.")
	m = p.findall(stdout)
	if m:
		print m

	totalsecondlength=int(m[0])

	print totalsecondlength

	pick_interval_second = INTERVAL_SECOND

	array_of_pickseconds = list(range(0,totalsecondlength,pick_interval_second))

	print array_of_pickseconds

	# conver the seconds to mm:ss format

	array_of_mmssformat =[]

	for item in array_of_pickseconds:
		mm=item/60
		ss=item%60
		result = str(mm)+':'+ format(ss,'02')
		array_of_mmssformat.append(result)

	print array_of_mmssformat


	for item in array_of_mmssformat:
		itemsplit=item.split(':')
		print itemsplit
		if specified_outputdir is not None:
			outputpath= specified_outputdir +"/"+videofilename +"-output-"+itemsplit[0]+"m"+itemsplit[1]+".jpg"
		else:
			outputpath= specified_outputdir +"/"+"output-"+itemsplit[0]+"m"+itemsplit[1]+".jpg"

		sscmd = "ffmpeg -ss "+item+" -i "+videofile + " -vframes 1 "+ outputpath
		print "sscmd="+sscmd
		process = subprocess.Popen(shlex.split(sscmd),stdout=DEVNULL,stderr=STDOUT)
		process.communicate()[0]

	return True