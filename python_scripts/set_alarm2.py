#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import sys
import os
import signal

# run the alarm
extProc = subprocess.Popen('env/bin/python3 ' + 'python_scripts/start_alarm2.py ' + str(sys.argv[1]) + " " + str(sys.argv[2]), stdout=subprocess.PIPE,
                           shell=True, preexec_fn=os.setpgrp)

print(os.getpgid(extProc.pid))
#print(os.getcwd())