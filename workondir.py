# find all vids in dir
# for each vid, to 'getcuts'


# provide option for separate dir for each vid
# or one unified output dir for all vids


import os
from os.path import isfile, join
import sampling
import argparse
import sys
import shutil
import common


DEFAULT_SAVEINONE_DIRNAME="saveallinone"



parser = argparse.ArgumentParser(description="video files batch screenshot sampling")
parser.add_argument('--saveinonedir',action='store_const', const=True, default=False,help="save all video screenshots in one directory")


parseargs = parser.parse_args()
print parseargs

saveinonedir_flag = parseargs.saveinonedir

print saveinonedir_flag



currentpath = os.getcwd()
allfileslist = [f for f in os.listdir(currentpath) if isfile(join(currentpath,f))]

# fetch only mp4, avi

allvidfiles = [f for f in allfileslist if common.containsvidextension( os.path.splitext(join(currentpath,f))[1])]

print "allvidfiles:"
print allvidfiles


totalvidfiles = len(allvidfiles)

# if saveinonedir_flag is true, then create unified outpudir
if saveinonedir_flag:
	# check if the saveallinone dir exists. if so, then remove it
	if os.path.isdir(join(currentpath,DEFAULT_SAVEINONE_DIRNAME)):
		print "removed saveinone dir"
		shutil.rmtree(join(currentpath,DEFAULT_SAVEINONE_DIRNAME))

	# create unified output dir
	os.makedirs(join(currentpath,DEFAULT_SAVEINONE_DIRNAME))


for index,f in enumerate(allvidfiles):
	print "working on %s / %s" % (index,totalvidfiles)
	if saveinonedir_flag:
		sampling.mainjob(f,specified_outputdir=DEFAULT_SAVEINONE_DIRNAME)
	else:
		sampling.mainjob(f)
