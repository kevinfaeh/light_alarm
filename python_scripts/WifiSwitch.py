#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import time


class Switch:
    """
    This class controls the mystrom switch.
    """

    def __init__(self, ip_address, mac_address):
        """
        This function initializes the bulb class.
        :param ip_address:
        :param mac_address:
        """
        self.__ip_address = ip_address
        self.__mac_address = mac_address

    def get_device_specifications(self, print_out=False):
        """
        This function returns device specifications
        :return: device specifications as dictionary
        :rtype: dict
        """
        command = 'curl --location --request GET  "' + self.__ip_address + '/api/v1/device"'
        device_specifications_json = os.popen(command).read()
        device_specifications_dict = json.loads(device_specifications_json)[self.__mac_address]
        if print_out == True:
            for key in device_specifications_dict:
                print(key + " : " + str(device_specifications_dict[key]))
        return device_specifications_dict

    def get_switch_report(self, print_out=False):
        """
        This function returns device specifications
        :return: device specifications as dictionary
        :rtype: dict
        """
        command = 'curl --location --request GET  "' + self.__ip_address + '/report"'
        device_specifications_json = os.popen(command).read()
        device_specifications_dict = json.loads(device_specifications_json)
        if print_out == True:
            for key in device_specifications_dict:
                print(key + " : " + str(device_specifications_dict[key]))
        return device_specifications_dict

    def turn_switch_on(self):
        """
        This function turns the switch on.
        """
        switch_status = self.get_switch_report()
        switch_state = switch_status["relay"]
        if switch_state == True:
            print("Switch is alredy on!")
            return
        else:
            command = 'curl --location --request GET "http://' + self.__ip_address + '/relay?state=1"'
            os.system(command)

    def turn_switch_off(self):
        """
        This function turns the switch off.
        """
        switch_status = self.get_switch_report()
        switch_state = switch_status["relay"]
        if switch_state == False:
            print("Switch is alredy off!")
            return
        else:
            command = 'curl --location --request GET "http://' + self.__ip_address + '/relay?state=0"'
            os.system(command)

    def toggle_switch(self):
        """
        This function changes the state of the switch and returns if it is now on or off
        :return:
        """
        command = 'curl --location --request GET  "' + self.__ip_address + '/toggle"'
        switch_state_json = os.popen(command).read()
        switch_state = json.loads(switch_state_json)["relay"]
        return switch_state

    def get_switch_status(self):
        """
        This function returns the room temperature rounded on 1 decimal digit
        :return:
        """
        switch_status = self.get_switch_report()
        switch_state = switch_status["relay"]
        return switch_state

    def get_room_temperature(self):
        """
        This function returns the room temperature rounded on 1 decimal digit
        :return:
        """
        switch_status = self.get_switch_report()
        room_temperature = float(switch_status["temperature"])
        return round(room_temperature, 1)

    def get_power_usage(self):
        """
        This function returns the power usage of the atached device
        :return:
        """
        switch_status = self.get_switch_report()
        power_usage = float(switch_status["power"])
        return round(power_usage, 1)

switch_ip = "192.168.8.116"
switch_mac = "A4CF12458620"
#
switch = Switch(switch_ip, switch_ip)

# switch.get_room_temperature()
# switch.get_switch_report(print_out=True)
# switch.turn_switch_off()
# switch.get_power_usage()
# switch.get_switch_status()





