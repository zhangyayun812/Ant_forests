# -*- coding: utf-8 -*-
"""
读取配置文件和屏幕分辨率
"""

import os
import sys
import re


def _get_screen_size():
    """
    获取手机屏幕大小
    """
    size_str = os.popen('adb shell wm size').read()
    if not size_str:
        print('请安装 ADB 及驱动并配置环境变量')
        sys.exit()
    m = re.search(r'(\d+)x(\d+)', size_str)
    # match()函数只检测RE是不是在string的开始位置匹配,search()会扫描整个string查找匹配,会扫描整个字符串并返回第一个成功的匹配,也就是说match（）只有在0位置匹配成功的话才有返回，如果不是开始位置匹配成功的话，match()就返回none
    if m:
        return "{height}x{width}".format(height=m.group(2), width=m.group(1))
        # group(1)列出search时第一个括号匹配部分,group(2)列出search时第二个括号匹配部分
    return "1920x1080"


