# -*- coding: utf-8 -*-
"""
唤醒手机并进入应用APP中
"""

import time
import traceback
import os
import re
from common import log_tools

def wake_up_only():
    """
    打开app
    """
    try:
        display_power_tate = "".join(re.findall(r'Display Power: state=\w+', os.popen(
            # 'adb shell dumpsys power | findstr "Display/C Power: state=" ').read()
            'adb shell dumpsys power').read())).split("=")[1]
        log_tools.log('info',display_power_tate)
        if display_power_tate == 'OFF':
            log_tools.log('info', "唤醒屏幕")
            os.system('adb shell input keyevent 26')
        else:
            log_tools.log('info',"屏幕已开启不需要唤醒")
        is_status_bar_keyguard = "".join(re.findall(r'isStatusBarKeyguard=\w+', os.popen(
            "adb shell dumpsys window policy").read())).split("=")[1]
        log_tools.log('info',is_status_bar_keyguard)
        if is_status_bar_keyguard == 'true':
            time.sleep(2)
            log_tools.log('info',"解锁屏保")
            # 左右滑动才好解锁,并且延迟100ms启动
            os.system('adb shell input swipe 200 400 800 400 100')
            time.sleep(1)
            os.system('adb shell input swipe 200 400 800 400 100')
            time.sleep(1)
            log_tools.log('info',"输入密码")
            os.system('adb shell input text 95729')
        else:
            log_tools.log('info',"屏幕已解锁不需要再次解锁")
        time.sleep(1)
    except Exception:
        log_tools.log('warning',"screenshot_prepare error")
        traceback.print_exc()
        exit(-1)
