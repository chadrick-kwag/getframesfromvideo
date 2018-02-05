# count the duration of all the vids in directory

#python2

# get all vid files

import common
import os

vidfiles = common.getallvidfiles(os.getcwd())

# print vidfiles

accumulate=0

for f in vidfiles:
	accumulate= accumulate+ common.getduration(f)

print accumulate
