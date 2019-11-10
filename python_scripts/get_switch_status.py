#!/usr/bin/env python
# -*- coding: utf-8 -*-

from WifiSwitch import switch

status = switch.get_switch_status()
print(status)
