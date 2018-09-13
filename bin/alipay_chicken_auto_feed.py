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
    """
    主函数
    """

    log_tools.log('info', '程序版本号：{}'.format(VERSION))

    # 唤醒屏幕-输入密码并进入到对应app
    wake_up.screenshot_prepare()
    try:
        # 获取庄园两个字后进入到对应应用模块
        time.sleep(3)
        # 开始截图
        now_times = datetime.datetime.now().strftime('%H-%M-%S')
        screenshot.check_screenshot('{}screen.png'.format(now_times))
        # 查找图片中坐标位置,截图后的原点在左下角
        positions = baiOcr.get_position("庄园", "..\\file\\{}screen.png".format(now_times))

        position_x = int(positions[0])
        position_y = int(positions[1])

        adb_tools.tap_by_xy(position_x, position_y)
    except IndexError:
        # 如果已经启动了APP，且没有在首页就重启APP
        wake_up.app_restart()
        try:
            time.sleep(3)
            # 开始截图
            now_times = datetime.datetime.now().strftime('%H-%M-%S')
            screenshot.check_screenshot('{}screen.png'.format(now_times))

            # 查找图片中坐标位置,截图后的原点在左下角
            positions = baiOcr.get_position("庄园", "..\\file\\{}screen.png".format(now_times))

            position_x = int(positions[0])
            position_y = int(positions[1])

            adb_tools.tap_by_xy(position_x, position_y)
        except IndexError:
            time.sleep(3)
            # 开始截图
            now_times = datetime.datetime.now().strftime('%H-%M-%S')
            screenshot.check_screenshot('{}screen.png'.format(now_times))

            # 查找图片中坐标位置,截图后的原点在左下角
            positions = baiOcr.get_position("庄园", "..\\file\\{}screen.png".format(now_times))

            position_x = int(positions[0])
            position_y = int(positions[1])

            adb_tools.tap_by_xy(position_x, position_y)

  
    
    
    # 判断当前是否在进行进食
    time.sleep(3)
    now_time = datetime.datetime.now().strftime('%H:%M')
    log_tools.log('info', now_time)

    now_times = datetime.datetime.now().strftime('%H-%M-%S')
    screenshot.check_screenshot("{}screen-more.png".format(now_times))
    positions = baiOcr.get_position("出去散心", "..\\file\\{}screen-more.png".format(now_times))
    if len(positions) != 0:
        log_tools.log('info', "小鸡不在了，请人工找回")
        exit(-1)

    else:
        positions = baiOcr.get_position("进食剩余", "..\\file\\{}screen-more.png".format(now_times))

        if len(positions) != 0:
            log_tools.log('info', "当前还有吃的不需要喂食！")

        # 找到粮食进行喂养
        else:
            # now_times = datetime.datetime.now().strftime('%H-%M-%S')
            # screenshot.check_screenshot("{}screen-more.png".format(now_times))
            positions = baiOcr.get_position("g", "..\\file\\{}screen-more.png".format(now_times))
            if len(positions) == 0:
                log_tools.log('info',"…当前没有食物喂养")
            else:
                position_x = int(positions[0])
                position_y = int(positions[1]) - 60
                adb_tools.tap_by_xy(position_x, position_y)
                log_tools.log('info', "…已尝试进行喂养")
                time.sleep(2)

                # 喂养后点击道具
                now_times = datetime.datetime.now().strftime('%H-%M-%S')
                screenshot.check_screenshot("{}screen-more.png".format(now_times))
                positions = baiOcr.get_position("道具", "..\\file\\{}screen-more.png".format(now_times))
                if len(positions) == 0:
                    log_tools.log('info',"……未找到道具按钮")
                else:
                    position_x = int(positions[0])
                    position_y = int(positions[1]) - 50
                    adb_tools.tap_by_xy(position_x, position_y)
                    log_tools.log('info', "……已进入道具道具")
                    time.sleep(2)

                    # 在道具界面使用道具
                    now_times = datetime.datetime.now().strftime('%H-%M-%S')
                    screenshot.check_screenshot("{}screen-more.png".format(now_times))
                    positions = baiOcr.get_position("使用道具", "..\\file\\{}screen-more.png".format(now_times))

                    if len(positions) == 0:
                        log_tools.log('info', "…………在道具界面未找到道具")
                    else:
                        position_x = int(positions[0])
                        position_y = int(positions[1])
                        adb_tools.tap_by_xy(position_x, position_y)
                        log_tools.log('info', "…………已使用加速道具")
            
            


if __name__ == '__main__':
    main()
