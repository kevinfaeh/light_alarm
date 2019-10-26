#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import sys
import os
import signal

# run the alarm
extProc = subprocess.Popen(['python3', 'start_alarm.py', str(sys.argv[1]), str(sys.argv[2])], stdout=subprocess.PIPE,
                           shell=False, preexec_fn=os.setpgrp)

print(os.getpgid(extProc.pid))
