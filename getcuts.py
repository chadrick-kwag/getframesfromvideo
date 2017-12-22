from subprocess import call
import subprocess
import sys
import re
import shlex

# check the duration of video first

videofile = sys.argv[1]

print videofile

# call(['ffmpeg','-i',videofile,'\|','grep','\"Duration\"'])
# cmdstr = "ffmpeg -i " + videofile + " | grep Duration"
cmdstr = "ffprobe -i " + videofile + " -show_entries format=duration -v quiet -of csv=\"p=0\""
# output1 = call(cmdstr,shell=True)
process = subprocess.Popen(shlex.split(cmdstr), stdout = subprocess.PIPE)

stdout = process.communicate()[0]
print 'STDOUT:{}'.format(stdout)




p = re.compile("(.+)\.")
m = p.findall(stdout)
if m:
	print m

totalsecondlength=int(m[0])

print totalsecondlength

pick_interval_second = 3

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

	sscmd = "ffmpeg -ss "+item+" -i "+videofile + " -vframes 1 "+ "output-"+itemsplit[0]+"m"+itemsplit[1]+".jpg"
	print "sscmd="+sscmd
	process = subprocess.Popen(shlex.split(sscmd))
	process.communicate()[0]



