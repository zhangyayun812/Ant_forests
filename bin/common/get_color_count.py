# -*- coding: utf-8 -*-
"""
唤醒手机并进入应用APP中
"""

import time

from common import log_tools
from PIL import Image

def get_color_count(img_name):
    """
    查找出图像中对应RGB像素
    """
    im_self = Image.open(img_name)
    self_energy_point_count = 0
    self_energy_point_boolean = False
    self_energy_position_handx = 0
    self_energy_position_handy = 0
    self_energy_w, self_energy_h = im_self.size
    self_operator_energy_point_list = []
    for self_energy_i in range(0, self_energy_w):
        self_energy_point_boolean = False
        for self_energy_j in range(0, int(self_energy_h)):
            pixel = im_self.getpixel((self_energy_i, self_energy_j))

            if pixel[0] == 132 and pixel[1] == 75 and pixel[2] == 40:
                # print(pixel)
                self_energy_point_count += 1
                self_energy_position_handx += self_energy_i
                self_energy_position_handy += self_energy_j
                self_energy_point_boolean = True

        if (not self_energy_point_boolean) and self_energy_point_count != 0 and self_energy_point_count > 200:
            log_tools.log('info', "current self_energy_point_count {}".format(self_energy_point_count))
            log_tools.log('info', "--Found self_energy points")
            self_energy_position_handx = round(self_energy_position_handx / self_energy_point_count, 0)
            self_energy_position_handy = round(self_energy_position_handy / self_energy_point_count, 0)
            self_operator_energy_point_list.append(self_energy_position_handx)
            self_operator_energy_point_list.append(self_energy_position_handy)
            self_energy_position_handx = 0
            self_energy_position_handy = 0
            self_energy_point_count = 0
            self_energy_point_boolean = False

    for self_energy_ii in range(0, len(self_operator_energy_point_list) - 1, 2):
        print(self_operator_energy_point_list[self_energy_ii],
                            self_operator_energy_point_list[self_energy_ii + 1])
        time.sleep(1)

def get_color_count_all(img_name):
    """
    查找出图像中对应RGB像素
    """
    im_self = Image.open(img_name)
    self_energy_point_count = 0
    self_energy_point_boolean = False
    self_energy_position_handx = 0
    self_energy_position_handy = 0
    self_energy_w, self_energy_h = im_self.size
    self_operator_energy_point_list = []
    for self_energy_i in range(0, self_energy_w):
        self_energy_point_boolean = False
        for self_energy_j in range(0, int(self_energy_h)):
            pixel = im_self.getpixel((self_energy_i, self_energy_j))

            print("{} {} {}".format(self_energy_i, self_energy_j, pixel))



if __name__ == '__main__':
    get_color_count("..\\..\\file\\yun.jpg")
    #get_color_count_all("..\\..\\file\\07-17-24screen-self.png")