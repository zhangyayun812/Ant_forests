# -*- coding: utf-8 -*-
"""
调取配置文件和屏幕分辨率的代码
"""
import time
import datetime
from common import log_tools
from PIL import Image

try:
    from common import config, screenshot, debug, baiOcr, wake_up, adb_tools
except Exception as ex:
    print(ex)
    print('请将脚本放在项目根目录中运行')
    print('请检查项目根目录中的 common 文件夹是否存在')
    exit(-1)

VERSION = "1.1.1"


def main():
    # 唤醒屏幕-输入密码并进入到对应app
    wake_up.wake_up_only()
    # print("wake_up end")
    adb_tools.keyevent_by_num(3)
    adb_tools.keyevent_by_num(3)

    # print("start screenshot")
    now_times = datetime.datetime.now().strftime('%H-%M-%S')
    screenshot.check_screenshot('{}screen.png'.format(now_times))
    # 查找图片中坐标位置,截图后的原点在左下角
    positions = baiOcr.get_position("Union Pay", "..\\file\\{}screen.png".format(now_times))
    position_x = int(positions[0])
    position_y = int(positions[1])
    adb_tools.tap_by_xy(position_x, position_y)

    now_times = datetime.datetime.now().strftime('%H-%M-%S')
    screenshot.check_screenshot('{}screen.png'.format(now_times))
    positions = baiOcr.get_position("签到", "..\\file\\{}screen.png".format(now_times))
    position_x = int(positions[0])
    position_y = int(positions[1])
    adb_tools.tap_by_xy(position_x, position_y)



if __name__ == '__main__':
    main()
