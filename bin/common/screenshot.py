# -*- coding: utf-8 -*-
"""
手机屏幕截图的代码
"""
import subprocess
import os
import sys
from PIL import Image
import time

# SCREENSHOT_WAY 是截图方法，经过 check_screenshot 后，会自动递减，不需手动修改
SCREENSHOT_WAY = 3


def pull_screenshot(img_name):
    screenshot_str = 'adb shell screencap -p /sdcard/{}'.format(img_name)
    # print(screenshot_str)
    pull_str = 'adb pull /sdcard/{} ..\\file'.format(img_name)
    # print(pull_str)
    os.system(screenshot_str)
    os.system(pull_str)

def check_screenshot(img_name):
    """
    检查获取截图的方式
    """
    if os.path.isfile('..\\..\\file\\{}'.format(img_name)):
        try:
            os.remove('..\\..\\file\\{}'.format(img_name))
        except Exception:
            pass

    pull_screenshot(img_name)
