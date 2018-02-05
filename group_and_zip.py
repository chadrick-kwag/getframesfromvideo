# zip in bunche
# python 2

# fetch all jpg files

import common
import os
import argparse
import sys


GROUP_SIZE=100



parser = argparse.ArgumentParser(description="zipping bunch of imagefiles into partial zip files")
parser.add_argument('--zipbasename',action='store', default="outputzip", help="zip file base name")

parseargs = parser.parse_args()

print parseargs.zipbasename




imgfiles = common.getallimagefiles(os.getcwd())

for i in range(0,len(imgfiles)/GROUP_SIZE +1):
	startlimit=100*i
	endlimit=100*(i+1)
	if endlimit > len(imgfiles):
		endlimit = len(imgfiles)

	grouplist=imgfiles[startlimit:endlimit]

	# print "%s th group size=%s" % (i,len(grouplist))

	zipfilename= parseargs.zipbasename + "-" + str(i)+".zip"

	common.create_zip(zipfilename,grouplist)
	print "%s zipping done" % (i)

print "finished"








