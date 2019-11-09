#!/usr/bin/env python
# -*- coding: utf-8 -*-


with open("python_scripts/bulb_data.txt", 'r+') as data:
    text = data.read()
    if text == "No Alarm Set":
        print(False)
    else:
        print(str(text))
    data.close()