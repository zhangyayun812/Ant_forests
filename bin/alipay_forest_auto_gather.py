# -*- coding: utf-8 -*-
"""
调取配置文件和屏幕分辨率的代码
"""
import time
# import pdb
import datetime
# import schedule
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


# 设置，设置保存在 config 文件夹中
# config = config.open_accordant_config()


def main():
    # def job():
    """
    主函数
    """

    # print('程序版本号：{}'.format(VERSION))
    log_tools.log('info', '程序版本号：{}'.format(VERSION))
    # 打印环境信息

    # debug.dump_device_info()
    # 获取屏幕并进入到对应app
    wake_up.screenshot_prepare()
    try:
        time.sleep(3)
        # 开始截图
        now_times = datetime.datetime.now().strftime('%H-%M-%S')
        screenshot.check_screenshot('{}screen.png'.format(now_times))
        # 查找图片中坐标位置,截图后的原点在左下角
        positions = baiOcr.get_position("森林", "..\\file\\{}screen.png".format(now_times))

        position_x = int(positions[0])
        position_y = int(positions[1])

        adb_tools.tap_by_xy(position_x, position_y)
    except IndexError:
        wake_up.app_restart()
        try:
            time.sleep(3)
            # 开始截图
            now_times = datetime.datetime.now().strftime('%H-%M-%S')
            screenshot.check_screenshot('{}screen.png'.format(now_times))

            # 查找图片中坐标位置,截图后的原点在左下角
            positions = baiOcr.get_position("森林", "..\\file\\{}screen.png".format(now_times))

            position_x = int(positions[0])
            position_y = int(positions[1])

            adb_tools.tap_by_xy(position_x, position_y)
        except IndexError:
            time.sleep(3)
            # 开始截图
            now_times = datetime.datetime.now().strftime('%H-%M-%S')
            screenshot.check_screenshot('{}screen.png'.format(now_times))

            # 查找图片中坐标位置,截图后的原点在左下角
            positions = baiOcr.get_position("森林", "..\\file\\{}screen.png".format(now_times))

            position_x = int(positions[0])
            position_y = int(positions[1])

            adb_tools.tap_by_xy(position_x, position_y)

        # time.sleep(3)
        ##开始截图
        # log_tools.log('warning', "except")
        # nowTimes = datetime.datetime.now().strftime('%H-%M-%S')
        # screenshot.check_screenshot('{}screen.png'.format(nowTimes))

        #
        ##查找图片中坐标位置,截图后的原点在左下角
        # positions = get_position.get_position("森林","..\\file\\{}screen.png".format(nowTimes))

        # position_x = (int(positions[0][1])+int(positions[1][1]))/2
        # position_y = ((int(debug.get_device_screen_width())-int(positions[0][2]))+(int(debug.get_device_screen_width())-int(positions[1][2])))/2

        # adb_tools.tap_by_xy(position_x, position_y)

    # 截取当前屏幕并查出可收取手型坐标
    green_point_count = 0
    green_point_boolean = False
    position_handx = 0
    position_handy = 0
    circulation = True
    count_self = 0
    count_detail = True

    while circulation:
        now_time = datetime.datetime.now().strftime('%H:%M')
        # nowTime = datetime.datetime.now().strftime('%M')
        log_tools.log('info', now_time)
        if now_time == '07:17' or now_time == '07:18' or now_time == '07:19':
            # if nowTime == '20' or nowTime == '21' or nowTime == '22' or nowTime == '23':
            # adb_tools.swipe_by_2point(100, 2000, 100, 300)
            # if nowTime == '23:06' or nowTime == '23:07' or nowTime == '23:08':
            count_detail = True
            # time.sleep(2)
            # screenshot.check_screenshot("screen-more.png")
            # positions = get_position.get_position("更多","screen-more.png")
            if count_self == 0:
                time.sleep(2)
                now_times = datetime.datetime.now().strftime('%H-%M-%S')
                screenshot.check_screenshot("{}screen-more.png".format(now_times))
                positions = baiOcr.get_position("查看", "..\\file\\{}screen-more.png".format(now_times))
                if len(positions) == 0:
                    log_tools.log('info', "返回上一级，准备收取自己")
                    adb_tools.keyevent_by_num(4)
                    time.sleep(2)
                log_tools.log('info', "--------------------进入自己界面")
                adb_tools.swipe_by_2point(100, 300, 100, 2000)
            time.sleep(2)
            adb_tools.swipe_by_2point(100, 300, 100, 2000)
            log_tools.log('info', "开始截自己图")
            now_times = datetime.datetime.now().strftime('%H-%M-%S')
            screenshot.pull_screenshot("{}screen-self.png".format(now_times))
            im_self = Image.open('..\\file\\{}screen-self.png'.format(now_times))
            self_energy_point_count = 0
            self_energy_point_boolean = False
            self_energy_position_handx = 0
            self_energy_position_handy = 0
            self_energy_w, self_energy_h = im_self.size
            self_operator_energy_point_list = []
            for self_energy_i in range(0, self_energy_w):
                self_energy_point_boolean = False
                for self_energy_j in range(0, int(self_energy_h / 2)):
                    pixel = im_self.getpixel((self_energy_i, self_energy_j))

                    if pixel[0] == 180 and pixel[1] == 240 and pixel[2] == 32:
                        # print(pixel)
                        self_energy_point_count += 1
                        # print('{} {} {} 是energy'.format(self_energy_i, self_energy_j, pixel))
                        self_energy_position_handx += self_energy_i
                        self_energy_position_handy += self_energy_j
                        self_energy_point_boolean = True
                    # print('{} {} {} 是energy'.format(self_energy_i, self_energy_j, pixel))

                if (not self_energy_point_boolean) and self_energy_point_count != 0 and self_energy_point_count > 200:
                    log_tools.log('info', "current self_energy_point_count {}".format(self_energy_point_count))
                    log_tools.log('info', "--Found self_energy points")
                    self_energy_position_handx = round(self_energy_position_handx / self_energy_point_count, 0)
                    self_energy_position_handy = round(self_energy_position_handy / self_energy_point_count, 0)
                    # print('{} {} {} {}'.format(self_position_handx, self_position_handy, i, j))
                    self_operator_energy_point_list.append(self_energy_position_handx)
                    self_operator_energy_point_list.append(self_energy_position_handy)
                    self_energy_position_handx = 0
                    self_energy_position_handy = 0
                    self_energy_point_count = 0
                    self_energy_point_boolean = False
                # if green_point_count

            for self_energy_ii in range(0, len(self_operator_energy_point_list) - 1, 2):
                log_tools.log('info', "进行收取")
                adb_tools.tap_by_xy(self_operator_energy_point_list[self_energy_ii],
                                    self_operator_energy_point_list[self_energy_ii + 1])
                time.sleep(3)
            log_tools.log('info', "--------第{}检查完自己的能量".format(count_self))
            count_self += 1


        else:
            if count_detail:
                time.sleep(8)
                adb_tools.swipe_by_2point(100, 1600, 100, 100)

                # 进入森林后开始向下滑动
                try:
                    time.sleep(2)
                    now_times = datetime.datetime.now().strftime('%H-%M-%S')
                    screenshot.check_screenshot("{}screen-more.png".format(now_times))
                    positions = baiOcr.get_position("查看更多好友", "..\\file\\{}screen-more.png".format(now_times))

                    query_number = len(positions)
                    position_x = int(positions[0])
                    position_y = int(positions[1])
                    adb_tools.tap_by_xy(position_x, position_y)
                except IndexError:
                    wake_up.app_restart()
                    try:
                        time.sleep(3)
                        # 开始截图
                        now_times = datetime.datetime.now().strftime('%H-%M-%S')
                        screenshot.check_screenshot('{}screen.png'.format(now_times))

                        # 查找图片中坐标位置,截图后的原点在左下角
                        positions = baiOcr.get_position("森林", "..\\file\\{}screen.png".format(now_times))

                        position_x = int(positions[0])
                        position_y = int(positions[1])

                        adb_tools.tap_by_xy(position_x, position_y)
                    except IndexError:
                        time.sleep(3)
                        # 开始截图
                        now_times = datetime.datetime.now().strftime('%H-%M-%S')
                        screenshot.check_screenshot('{}screen.png'.format(now_times))

                        # 查找图片中坐标位置,截图后的原点在左下角
                        positions = baiOcr.get_position("森林", "..\\file\\{}screen.png".format(now_times))

                        position_x = int(positions[0])
                        position_y = int(positions[1])

                        adb_tools.tap_by_xy(position_x, position_y)

                    # 截取当前屏幕并查出可收取手型坐标
                    green_point_count = 0
                    green_point_boolean = False
                    position_handx = 0
                    position_handy = 0
                    circulation = True
                    count_self = 0
                    count_detail = True
                    continue

                count_detail = False

                log_tools.log('info', "--------------------进入好友列表")
            else:
                time.sleep(2)
                now_times = datetime.datetime.now().strftime('%H-%M-%S')
                screenshot.pull_screenshot("{}screen-list.png".format(now_times))
                # 查找图片中坐标位置
                positions = baiOcr.get_position("多了", "..\\file\\{}screen-list.png".format(now_times))
                if len(positions) != 0:
                    log_tools.log('info', "当前页为最后一页")
                    # break
                    # circulation = False

                    time.sleep(1)
                    log_tools.log('info', "返回上一级，准备重新进入好友列表")
                    adb_tools.keyevent_by_num(4)
                    try:
                        time.sleep(2)
                        now_times = datetime.datetime.now().strftime('%H-%M-%S')
                        screenshot.check_screenshot("{}screen-more.png".format(now_times))
                        positions = baiOcr.get_position("查看更多好友", "..\\file\\{}screen-more.png".format(now_times))

                        position_x = int(positions[0])
                        position_y = int(positions[1])

                        log_tools.log('info', "--------------------再次进入好友列表")
                        adb_tools.tap_by_xy(position_x, position_y)
                    except IndexError:
                        wake_up.app_restart()
                        try:
                            time.sleep(3)
                            # 开始截图
                            now_times = datetime.datetime.now().strftime('%H-%M-%S')
                            screenshot.check_screenshot('{}screen.png'.format(now_times))

                            # 查找图片中坐标位置,截图后的原点在左下角
                            positions = baiOcr.get_position("森林", "..\\file\\{}screen.png".format(now_times))

                            position_x = int(positions[0])
                            position_y = int(positions[1])

                            adb_tools.tap_by_xy(position_x, position_y)
                        except IndexError:
                            time.sleep(3)
                            # 开始截图
                            now_times = datetime.datetime.now().strftime('%H-%M-%S')
                            screenshot.check_screenshot('{}screen.png'.format(now_times))

                            # 查找图片中坐标位置,截图后的原点在左下角
                            positions = baiOcr.get_position("森林", "..\\file\\{}screen.png".format(now_times))

                            position_x = int(positions[0])
                            position_y = int(positions[1])

                            adb_tools.tap_by_xy(position_x, position_y)

                        # 截取当前屏幕并查出可收取手型坐标
                        green_point_count = 0
                        green_point_boolean = False
                        position_handx = 0
                        position_handy = 0
                        circulation = True
                        count_self = 0
                        count_detail = True
                        continue

        time.sleep(2)
        now_times = datetime.datetime.now().strftime('%H-%M-%S')
        screenshot.pull_screenshot("{}screen-list.png".format(now_times))
        im = Image.open('..\\file\\{}screen-list.png'.format(now_times))
        w, h = im.size
        operator_point_list = []
        for i in range(0, h):
            green_point_boolean = False
            for j in range(800, w):
                pixel = im.getpixel((j, i))

                if (pixel[0] == 48) and (pixel[1] == 191) and (pixel[2] == 108):
                    # print(pixel)
                    green_point_count += 1
                    # print('{} {} {} 是green'.format(j, i, pixel))
                    position_handx += j
                    position_handy += i
                    green_point_boolean = True

            # 不添加大于1200会有误差判断

            if (not green_point_boolean) and (green_point_count != 0):
                log_tools.log('info', "current green_point_count {}".format(green_point_count))
                # print('{} {} {}'.format(position_handx, position_handy, i))
                log_tools.log('info', "--Found green points")
                if green_point_count < 2000 and green_point_count > 1600:
                    log_tools.log('info', "----Found green hand")
                    position_handx = round(position_handx / green_point_count, 0)
                    position_handy = round(position_handy / green_point_count, 0)
                    operator_point_list.append(position_handx)
                    operator_point_list.append(position_handy)
                else:
                    log_tools.log('info', "----Not found green hand")
                position_handx = 0
                position_handy = 0
                green_point_count = 0
                green_point_boolean = False

        log_tools.log('info', "检查完一张截屏,判断是否需要进入到好友森林界面")

        if len(operator_point_list) != 0:
            # 开始点击需要点击的点,并在点击后进行截图
            for i in range(0, len(operator_point_list) - 1, 2):
                log_tools.log('info', "进入到好友森林详情界面")
                adb_tools.tap_by_xy(operator_point_list[i], operator_point_list[i + 1])

                log_tools.log('info', "判断是否有能量可取")
                # 在详情界面进行截图并判断是否可获取
                time.sleep(2)
                now_times = datetime.datetime.now().strftime('%H-%M-%S')
                screenshot.pull_screenshot("{}screen-other.png".format(now_times))
                im_other = Image.open('..\\file\\{}screen-other.png'.format(now_times))
                energy_point_count = 0
                energy_point_boolean = False
                energy_position_handx = 0
                energy_position_handy = 0
                energy_w, energy_h = im_other.size
                operator_energy_point_list = []
                for energy_i in range(0, energy_w):
                    energy_point_boolean = False
                    for energy_j in range(0, int(energy_h / 2)):
                        pixel = im_other.getpixel((energy_i, energy_j))

                        if pixel[0] == 180 and pixel[1] == 240 and pixel[2] == 32:
                            # print(pixel)
                            energy_point_count += 1
                            # print('{} {} {} 是energy'.format(energy_i, energy_j, pixel))
                            energy_position_handx += energy_i
                            energy_position_handy += energy_j
                            energy_point_boolean = True
                        # print('{} {} {} 是energy'.format(energy_i, energy_j, pixel))

                    if (not energy_point_boolean) and energy_point_count != 0 and energy_point_count > 200:
                        log_tools.log('info', "current energy_point_count {}".format(energy_point_count))
                        log_tools.log('info', "--Found energy points")
                        energy_position_handx = round(energy_position_handx / energy_point_count, 0)
                        energy_position_handy = round(energy_position_handy / energy_point_count, 0)
                        # print('{} {} {} {}'.format(position_handx, position_handy, i, j))
                        operator_energy_point_list.append(energy_position_handx)
                        operator_energy_point_list.append(energy_position_handy)
                        energy_position_handx = 0
                        energy_position_handy = 0
                        energy_point_count = 0
                        energy_point_boolean = False
                    # if green_point_count

                for energy_ii in range(0, len(operator_energy_point_list) - 1, 2):
                    log_tools.log('info', "进行收取")
                    adb_tools.tap_by_xy(operator_energy_point_list[energy_ii],
                                        operator_energy_point_list[energy_ii + 1])
                    time.sleep(3)

                # 收取完能量后返回到列表中
                time.sleep(1)
                log_tools.log('info', "返回好友列表")
                adb_tools.keyevent_by_num(4)
                time.sleep(1)
        else:
            log_tools.log('info', "不需要进入好友森林详情")
        log_tools.log('info', "好友列表向下滑动")
        adb_tools.swipe_by_2point(100, 800, 100, 100)


    # schedule.every().day.at("07:00").do(job)


# schedule.every().day.at("21:55").do(job)

# while True:
#    schedule.run_pending()
#    time.sleep(1)


if __name__ == '__main__':
    main()
