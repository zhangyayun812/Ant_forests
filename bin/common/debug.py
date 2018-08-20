# -*- coding: utf-8 -*-
"""
这儿是debug的代码，当DEBUG_SWITCH开关开启的时候，会将各种信息存在本地，方便检查故障
"""
import os


def get_device_screen_width():
    size_str = os.popen('adb shell wm size').read()
    return size_str.split()[2].split('x')[1]


def get_device_screen_heigh():
    size_str = os.popen('adb shell wm size').read()
    return size_str.split()[2].split('x')[0]

