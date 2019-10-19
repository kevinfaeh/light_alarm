#!/usr/bin/env python
# -*- coding: utf-8 -*-

from WifiBulb import Bulb

bulb_ip = "192.168.8.114"
bulb_mac = "5CCF7FA0BB48"

bulb = Bulb()
device_specifications = bulb.get_device_specifications()
print(device_specifications['on'])