#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import time


class Bulb:
    """
    This class controls the mystrom bulb.
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

    def turn_light_on(self):
        """
        This function turns the light on.
        """
        device_specifications = self.get_device_specifications()
        ligth_status = device_specifications["on"]
        if ligth_status == True:
            print("Light is alredy on!")
            return
        else:
            command = 'curl --location --request POST "http://' + self.__ip_address + '/api/v1/device/' + self.__mac_address + '"' + ' --data  "action=on"'
            os.system(command)
            #time.sleep(2)

    def turn_light_off(self):
        """
        This function turns the light off.
        """
        device_specifications = self.get_device_specifications()
        ligth_status = device_specifications["on"]
        if ligth_status == False:
            print("Light is alredy off!")
            return
        else:
            command = 'curl --location --request POST "http://' + self.__ip_address + '/api/v1/device/' + self.__mac_address + '"' + ' --data  "action=off"'
            os.system(command)
            #time.sleep(2)

    def set_light_mode(self, mode):
        """
        This functions sets the light mode. We use hsv (hue, saturation, value)
        :param mode: string of mode ("hsv")
        :type str
        """
        command = 'curl --location --request POST "http://' + self.__ip_address + '/api/v1/device/' + self.__mac_address + '"' + ' --data  "mode=' + mode + '"'
        os.system(command)

    def set_color_hsv(self, hsv, transition_time=400):
        """
        This function sets the color of the bulb with hsv: hue: [0, 360], saturation [0, 100], value [0, 100]
        :param hsv: list with 3 values: h, s ,v
        :type hsv: list
        :param transition_time: time from current state to next state in ms.
        :type transition_time float
        """
        color = str(hsv[0]) + ";" + str(hsv[1]) + ";" + str(hsv[2])
        ramp = str(transition_time)
        command = 'curl --location --request POST "http://' + self.__ip_address + '/api/v1/device/' + self.__mac_address + '"' + ' --data  "color=' + color + '&ramp=' + ramp + '"'
        os.system(command)
        time.sleep(transition_time/1000)

    def rgb_to_hsv(self, rgb):
        """
        This function converts rgb to hsv values
        :param rgb: list of rgb values
        :return: hsv list of hsv values
        """
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]
        h = 0
        s = 0
        v = 0

        r, g, b = r / 255.0, g / 255.0, b / 255.0
        mx = max(r, g, b)
        mn = min(r, g, b)
        df = mx - mn
        if mx == mn:
            h = 0
        elif mx == r:
            h = int((60 * ((g - b) / df) + 360) % 360)
        elif mx == g:
            h = int((60 * ((b - r) / df) + 120) % 360)
        elif mx == b:
            h = int((60 * ((r - g) / df) + 240) % 360)
        if mx == 0:
            s = 0
        else:
            s = int(100 * df / mx)
        v = int(mx*100)
        hsv = [h, s, v]
        return hsv

    def hex_to_rgb(self, hexcolor):
        """
        This function converts the hexadecimal color to an rgb color.
        :param hexcolor: hexadecimal color
        :type hexcolor: stringS
        :return: rgb values
        :rtype: list
        """
        color = str(hexcolor)
        color_rgb = [int(color[i:i+2], 16) for i in (0, 2, 4)]
        return color_rgb

    def set_color_hex(self, hexcolor, transition_time=400):
        """
        This function sets the color of the bulb with hsv: hue: [0, 360], saturation [0, 100], value [0, 100]
        :param hexcolor: string as hexadecimal numbers
        :type hexcolor: string
        :param transition_time: time from current state to next state in ms.
        :type transition_time float
        """
        color_rgb = self.hex_to_rgb(hexcolor)
        color_hsv = self.rgb_to_hsv(color_rgb)
        print(color_hsv)
        self.set_color_hsv(color_hsv)


bulb_ip = "192.168.8.115"
bulb_mac = "68C63AD021B2"
#
bulb = Bulb(bulb_ip, bulb_mac)
# this shows how to use it

# bulb.set_light_mode("hsv")
# # bulb.get_device_specifications(print_out=True)
# # hsv_value = [3, 50, 50]
# # bulb.set_color_hsv(hsv_value, 300)
# bulb.turn_light_on()
# bulb.get_device_specifications(print_out=True)
# spec = bulb.get_device_specifications(print_out=True)
# print(spec['on'])




