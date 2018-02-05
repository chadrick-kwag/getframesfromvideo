from subprocess import call
import subprocess
import sys
import re
import shlex
import os
import sampling

## usage
## using python2
## python getcuts.py <videofile>

# check the duration of video first

videofile = sys.argv[1]


sampling.mainjob(videofile)

