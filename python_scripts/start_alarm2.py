#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import datetime
import pygame

from WifiBulb import bulb


alarm_time = str(sys.argv[1])
alarm_durance = int(sys.argv[2])
alarm_durance_sec = 60 * alarm_durance
wait_time = alarm_durance_sec / 10
wakeup_colors = ["480000", "640000" "9C0003", "CA4106", "8D2204", "882F1B", "833918", "DF8B04", "C5AA84", "FFF1D2"]

with open("python_scripts/bulb_data.txt", 'w+') as data:
    data.write(alarm_time)
    #print("wrote data")
    data.close()
    time.sleep(0.2)


def check_if_break(alarm_time):
    """
    This function checks if the alarm should stop
    :return:
    """
    with open("python_scripts/bulb_data.txt", 'r+') as data:
        read_alarm_time = data.read()
        #print(read_alarm_time)
        data.close()
        if read_alarm_time != alarm_time:
            return True
        else:
            return False


while True:
    time_now = datetime.datetime.now()
    if len(str(time_now.hour)) < 2:
        hour = "0" + str(time_now.hour)
    else:
        hour = str(time_now.hour)
    if len(str(time_now.minute)) < 2:
        minute = "0" + str(time_now.minute)
    else:
        minute = str(time_now.minute)

    if check_if_break(alarm_time):
        break

    if hour == str(alarm_time[0:2]) and minute == str(alarm_time[3:5]):
        bulb.turn_light_on()
        for i in range(9):
            bulb.set_color_hex(wakeup_colors[i])
            if check_if_break(alarm_time):
                break
            if i == 6:
                pygame.mixer.init()
                sound = pygame.mixer.Sound("python_scripts/sound/bird.wav")
                sound.play()
            time.sleep(wait_time)
        pygame.mixer.init()
        sound = pygame.mixer.Sound("python_scripts/sound/marimba.wav")
        for i in range(10):
            if check_if_break(alarm_time):
                break
            sound.play()
            time.sleep(4)
        break
    time.sleep(5)

with open("python_scripts/bulb_data.txt", 'w+') as data:
    data.write(alarm_time)
    print("No Alarm Set")
    data.close()