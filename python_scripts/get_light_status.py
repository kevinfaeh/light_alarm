#!/usr/bin/env python
# -*- coding: utf-8 -*-

from WifiBulb import bulb

device_specifications = bulb.get_device_specifications()
print(device_specifications['on'])