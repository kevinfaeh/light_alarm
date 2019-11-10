#!/usr/bin/env python
# -*- coding: utf-8 -*-

from WifiSwitch import switch

temperature = switch.get_room_temperature()
print(temperature)