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
        # 获取森林两个字后进入到对应应用模块
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
        # 如果已经启动了APP，且没有在首页就重启APP
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

    # 进入到森林后循环收取能量
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
        log_tools.log('info', now_time)
        #time.sleep(2)


        # 时间是17分到19分就一直截取自己准备进行收取
        if now_time == '07:17' or now_time == '07:18' or now_time == '07:19':
        #if now_time == '20:05' or now_time == '07:18':
            count_detail = True
            # 如果count_self为0代表为第一次收取自己，如果不是第一次就直接截图不用判断是否在好友列表
            if count_self == 0:
                ## time.sleep(2)
                now_times = datetime.datetime.now().strftime('%H-%M-%S')
                screenshot.check_screenshot("{}screen-more.png".format(now_times))
                positions = baiOcr.get_position("排行", "..\\file\\{}screen-more.png".format(now_times))
                if len(positions) != 0:
                    log_tools.log('info', "返回上一级，准备收取自己")
                    adb_tools.keyevent_by_num(4)
                    time.sleep(2)
                log_tools.log('info', "--------------------进入自己界面")
                adb_tools.swipe_by_2point(100, 400, 100, 2000)
                time.sleep(1)
                adb_tools.swipe_by_2point(100, 400, 100, 2000)
                time.sleep(1)
                #经常有提示合种浇水，所以先点击一次关闭
                adb_tools.tap_by_xy(138, 688)
                time.sleep(1)
                #经常有提示合种浇水，所以先点击一次关闭
                adb_tools.tap_by_xy(137, 731)



            ## time.sleep(2)
            adb_tools.swipe_by_2point(100, 400, 100, 2000)
            log_tools.log('info', "开始截自己图")
            now_times = datetime.datetime.now().strftime('%H-%M-%S')
            screenshot.pull_screenshot("{}screen-self.png".format(now_times))
            # im_self = Image.open('..\\file\\{}screen-self.png'.format(now_times))
            # self_energy_point_count = 0
            # self_energy_point_boolean = False
            # self_energy_position_handx = 0
            # self_energy_position_handy = 0
            # self_energy_w, self_energy_h = im_self.size
            # self_operator_energy_point_list = []
            # for self_energy_i in range(0, self_energy_w):
            #     self_energy_point_boolean = False
            #     for self_energy_j in range(0, int(self_energy_h / 2)):
            #         pixel = im_self.getpixel((self_energy_i, self_energy_j))
            #
            #         if pixel[0] == 180 and pixel[1] == 240 and pixel[2] == 32:
            #             # print(pixel)
            #             self_energy_point_count += 1
            #             self_energy_position_handx += self_energy_i
            #             self_energy_position_handy += self_energy_j
            #             self_energy_point_boolean = True
            #
            #     if (not self_energy_point_boolean) and self_energy_point_count != 0 and self_energy_point_count > 200:
            #         log_tools.log('info', "current self_energy_point_count {}".format(self_energy_point_count))
            #         log_tools.log('info', "--Found self_energy points")
            #         self_energy_position_handx = round(self_energy_position_handx / self_energy_point_count, 0)
            #         self_energy_position_handy = round(self_energy_position_handy / self_energy_point_count, 0)
            #         self_operator_energy_point_list.append(self_energy_position_handx)
            #         self_operator_energy_point_list.append(self_energy_position_handy)
            #         self_energy_position_handx = 0
            #         self_energy_position_handy = 0
            #         self_energy_point_count = 0
            #         self_energy_point_boolean = False

            # for self_energy_ii in range(0, len(self_operator_energy_point_list) - 1, 2):
            #     log_tools.log('info', "进行收取")
            #     adb_tools.tap_by_xy(self_operator_energy_point_list[self_energy_ii],
            #                         self_operator_energy_point_list[self_energy_ii + 1])
            #     time.sleep(1)
            log_tools.log('info', "判断自己的行走是否有能量可取")
            positions = baiOcr.get_position("行走", "..\\file\\{}screen-self.png".format(now_times))
            if len(positions) != 0:
                log_tools.log('info', "进行收取")
                position_x = int(positions[0])
                position_y = int(positions[1]) - 80
                adb_tools.tap_by_xy(position_x, position_y)
            log_tools.log('info', "--------第{}检查完自己的能量".format(count_self))
            count_self += 1

        # 不在指定时间内就执行以下代码
        else:
            # count_detail第一次进入到森林，所以需要往下滑动。且滑动后需要将count_detail置为false代表已经进入到过森林
            if count_detail:
                time.sleep(10)
                adb_tools.swipe_by_2point(100, 1300, 100, 100)
                time.sleep(1)
                adb_tools.swipe_by_2point(100, 1300, 100, 100)

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

                    # 重启app后需要重置变量
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

            # 不是第一次进入到森林（说明是在好友列表）或已经进入好友列表，此时行判定是不是好友列表最后一页

            time.sleep(2)
            now_times = datetime.datetime.now().strftime('%H-%M-%S')
            screenshot.pull_screenshot("{}screen-list.png".format(now_times))
            # 查找图片中坐标位置是否有多了两个字
            positions = baiOcr.get_position("多了", "..\\file\\{}screen-list.png".format(now_times))
            if len(positions) != 0:
                    log_tools.log('info', "当前页为最后一页")
                    log_tools.log('info', "返回上一级，准备重新进入好友列表")
                    adb_tools.keyevent_by_num(4)
                    try:
                        time.sleep(2)
                        adb_tools.swipe_by_2point(100, 1300, 100, 100)
                        time.sleep(1)
                        adb_tools.swipe_by_2point(100, 1300, 100, 100)
                        now_times = datetime.datetime.now().strftime('%H-%M-%S')
                        screenshot.check_screenshot("{}screen-more.png".format(now_times))
                        positions = baiOcr.get_position("查看更多好友", "..\\file\\{}screen-more.png".format(now_times))

                        position_x = int(positions[0])
                        position_y = int(positions[1])

                        log_tools.log('info', "--------------------再次进入好友列表")
                        adb_tools.tap_by_xy(position_x, position_y)
                        time.sleep(2)
                        now_times = datetime.datetime.now().strftime('%H-%M-%S')
                        screenshot.pull_screenshot("{}screen-list.png".format(now_times))
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
                            time.sleep(2)
                            now_times = datetime.datetime.now().strftime('%H-%M-%S')
                            screenshot.pull_screenshot("{}screen-list.png".format(now_times))
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
                            time.sleep(2)
                            now_times = datetime.datetime.now().strftime('%H-%M-%S')
                            screenshot.pull_screenshot("{}screen-list.png".format(now_times))

                        # 截取当前屏幕并查出可收取手型坐标
                        green_point_count = 0
                        green_point_boolean = False
                        position_handx = 0
                        position_handy = 0
                        circulation = True
                        count_self = 0
                        count_detail = True
                        continue
            else:
                log_tools.log('info', "当前页不是最后一页，继续执行")

            # 在好友列表进行截图判定有没有可收取手型
            # 没有多了两个字就不需要重新截图

            # now_times = datetime.datetime.now().strftime('%H-%M-%S')
            # screenshot.pull_screenshot("{}screen-list.png".format(now_times))
            im = Image.open('..\\file\\{}screen-list.png'.format(now_times))
            w, h = im.size
            operator_point_list = []
            for i in range(0, h):
                green_point_boolean = False
                for j in range(800, w):
                    pixel = im.getpixel((j, i))

                    # if (pixel[0] == 48) and (pixel[1] == 191) and (pixel[2] == 108):
                    if (pixel[0] == 29) and (pixel[1] == 160) and (pixel[2] == 109):
                        green_point_count += 1
                        position_handx += j
                        position_handy += i
                        green_point_boolean = True

                # 不添加大于1200会有误差判断

                if (not green_point_boolean) and (green_point_count != 0):
                    log_tools.log('info', "current green_point_count {}".format(green_point_count))
                    # print('{} {} {}'.format(position_handx, position_handy, i))
                    log_tools.log('info', "--Found green points")
                    if green_point_count < 2000 and green_point_count > 1300:
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

            # 有手型就需要进入到对应好友森林详细界面
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
                    positions = baiOcr.get_position("可收取", "..\\file\\{}screen-other.png".format(now_times))
                    if len(positions) != 0:
                        for energy_ii in range(0, len(positions) - 1, 2):
                            log_tools.log('info', "进行收取")
                            position_x = int(positions[energy_ii])
                            position_y = int(positions[energy_ii + 1]) - 80
                            adb_tools.tap_by_xy(position_x, position_y)
                        # 收取完能量后返回到列表中
                        ## time.sleep(1)
                        log_tools.log('info', "返回好友列表")
                        adb_tools.keyevent_by_num(4)
                        time.sleep(1)
                        continue

                    # 通过可收取 三个字未找到能量时，采用对比颜色进行收取
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
                                energy_point_count += 1
                                energy_position_handx += energy_i
                                energy_position_handy += energy_j
                                energy_point_boolean = True
                            # print('{} {} {} 是energy'.format(energy_i, energy_j, pixel))

                        if (not energy_point_boolean) and energy_point_count != 0 and energy_point_count > 200:
                            log_tools.log('info', "current energy_point_count {}".format(energy_point_count))
                            log_tools.log('info', "--Found energy points")
                            energy_position_handx = round(energy_position_handx / energy_point_count, 0)
                            energy_position_handy = round(energy_position_handy / energy_point_count, 0)
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

                    # 收取完能量后返回到列表中
                    ## time.sleep(1)
                    log_tools.log('info', "返回好友列表")
                    adb_tools.keyevent_by_num(4)
                    time.sleep(1)
            else:
                log_tools.log('info', "不需要进入好友森林详情")
            log_tools.log('info', "好友列表向下滑动")
            adb_tools.swipe_by_2point(100, 900, 100, 100)


if __name__ == '__main__':
    main()
