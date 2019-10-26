#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import sys
import os
import signal

os.kill(int(sys.argv[1]), signal.SIGTERM)