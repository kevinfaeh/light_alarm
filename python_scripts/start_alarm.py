#!/usr/bin/env python
# -*- coding: utf-8 -*-

from WifiBulb import bulb
import sys
import time
import datetime
from pygame import mixer

alarm_time = str(sys.argv[1])
alarm_durance = int(sys.argv[2])
alarm_durance_sec = 60 * alarm_durance
wait_time = alarm_durance_sec / 10
wakeup_colors = ["480000", "640000" "9C0003", "CA4106", "8D2204", "882F1B", "833918", "DF8B04", "C5AA84", "FFF1D2"]


while True:
    time_now = datetime.datetime.now()
    if str(time_now.hour) == str(alarm_time[0:2]) and str(time_now.minute) == str(alarm_time[3:5]):
        bulb.turn_light_on()
        for i in range(9):
            bulb.set_color_hex(wakeup_colors[i])
            if i == 6:
                mixer.init()
                sound = mixer.Sound("python_scripts/sound/bird.wav")
                sound.play()
            time.sleep(wait_time)
        mixer.init()
        sound = mixer.Sound("python_scripts/sound/marimba.wav")
        for i in range(10):
            sound.play()
            time.sleep(4)
        break
    time.sleep(5)